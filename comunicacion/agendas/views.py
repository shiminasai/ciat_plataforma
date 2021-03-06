# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from models import *
from comunicacion.contrapartes.models import *
from forms import *
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.generic import generic_inlineformset_factory
from django.utils import simplejson
import datetime
from mapeo.models import Organizaciones
from analisis.configuracion.models import SitioAccion
from django.views.decorators.csrf import csrf_exempt
import thread
from django.contrib.sites.models import Site
from django.template.loader import render_to_string
from django.core.mail import send_mail, EmailMultiAlternatives
# Create your views here.

@login_required
def crear_agenda(request):
    if request.method == 'POST':
        form = AgendaForm(request.POST, request.FILES)
        form1 = DocuForm(request.POST, request.FILES)

        if form.is_valid() and form1.is_valid():
            form_uncommited = form.save(commit=False)
            form_uncommited.user = request.user
            form_uncommited.save()
            if form1.cleaned_data['nombre_doc'] != '':
                form1_uncommitd = form1.save(commit=False)
                form1_uncommitd.content_object = form_uncommited
                form1_uncommitd.save()
            thread.start_new_thread(notify_all_event, (form_uncommited,))
            return HttpResponseRedirect('/agendas/calendario')
    else:
        form = AgendaForm()
        form1 = DocuForm()
    return render_to_response('comunicacion/agendas/crear_agenda.html', locals(),
    	                         context_instance=RequestContext(request))

@login_required
def editar_agenda(request, id):
    agenda = get_object_or_404(Agendas, id=id)
    #agenda_type = ContentType.objects.get(app_label="foros",model="documentos")
    #docu = agenda_type.get_object_for_this_type(object_id=id)
    AgendaFormSet = generic_inlineformset_factory(Documentos, extra=2)
    form1 = AgendaFormSet(instance=agenda)

    if not agenda.user.userprofile.contraparte == request.user.userprofile.contraparte:
    	return HttpResponse("Usted no puede editar esta Agenda")

    if request.method == 'POST':
        form = AgendaForm(request.POST, instance = agenda)
        form1 = AgendaFormSet(data=request.POST, files=request.FILES, instance = agenda)
    	if form.is_valid() and form1.is_valid():
            form_uncommited = form.save(commit=False)
            form_uncommited.user = request.user
            form_uncommited.save()

            #form1_uncommitd = form1.save(commit=False)
            #form1_uncommitd.content_object = form_uncommited
            #form1_uncommitd.save()
            form1.save()
            return HttpResponseRedirect('/agendas/calendario/?shva=editada')
    else:
        form = AgendaForm(instance=agenda)
        form1 = AgendaFormSet(instance=agenda)
        
    return render_to_response('comunicacion/agendas/crear_agenda.html', locals(),
    	                         context_instance=RequestContext(request))

@login_required
def borrar_agenda(request, id):
    agenda = get_object_or_404(Agendas, pk=id)

    if agenda.user == request.user or request.user.is_superuser:
        agenda.delete()
        return redirect('/agendas/calendario/?shva=erase')
    else:
        return redirect('/')

@login_required
@csrf_exempt
def calendario(request,id=None):
    paises = Pais.objects.all()
    contrapartes = Organizaciones.objects.all()

    if request.is_ajax():
        start = datetime.datetime.fromtimestamp(float(request.GET['start']))
        end = datetime.datetime.fromtimestamp(float(request.GET['end']))
        fecha1 = datetime.date(start.year, start.month, start.day)
        fecha2 = datetime.date(end.year, end.month, end.day)
        
        eventos = Agendas.objects.filter(inicio__range=(fecha1, fecha2), user__userprofile__contraparte=request.user.userprofile.contraparte)
        var = []        
        for evento in eventos:
            d = {
                 'id': str(evento.id),
                 'title': u'%s' % (evento.evento), 
                 'start':str(evento.inicio), 
                 'end':str(evento.final), 
                 'allDay': True,
                 'color':str(evento.user.userprofile.contraparte.font_color)
                 }
            var.append(d)
        return HttpResponse(simplejson.dumps(var), mimetype='application/json')
    if not id==None:
        actividad = Agendas.objects.get(pk=id)
    #contrapartes_sel = Organizaciones.objects.filter(id__in=request.session['p'])
    #contrapartes_otras = Organizaciones.objects.exclude(id__in=request.session['p'])
    return render_to_response('comunicacion/agendas/agenda_list.html',locals(),
                              context_instance = RequestContext(request))
@csrf_exempt
def calendario_list(request):

    actividad = Agendas.objects.all

    return render_to_response('comunicacion/agendas/agenda_old_event.html',locals(),
                              context_instance = RequestContext(request))

@csrf_exempt
def calendario_publico(request,id=None):
    paises = SitioAccion.objects.all()
    contrapartes = Organizaciones.objects.exclude(plataforma__id=8).order_by('nombre')
    if request.is_ajax():
        start = datetime.datetime.fromtimestamp(float(request.GET['start']))
        end = datetime.datetime.fromtimestamp(float(request.GET['end']))
        fecha1 = datetime.date(start.year, start.month, start.day)
        fecha2 = datetime.date(end.year, end.month, end.day)
        
        eventos = Agendas.objects.filter(inicio__range=(fecha1, fecha2),publico=True)
        var = []        
        for evento in eventos:
            d = {
                 'id': str(evento.id),
                 'title': u'%s' % (evento.evento), 
                 'start':str(evento.inicio), 
                 'end':str(evento.final), 
                 'allDay': True,
                 'color':str(evento.user.userprofile.contraparte.font_color),
                 }
            var.append(d)
        return HttpResponse(simplejson.dumps(var), mimetype='application/json')

    if not id==None:
        actividad = Agendas.objects.get(pk=id)
    
    return render_to_response('comunicacion/agendas/agenda_list_public.html',locals(),
                              context_instance = RequestContext(request))

@csrf_exempt
def calendario_publico_sitio(request,id_sitio=None):
    paises = SitioAccion.objects.all()
    #contrapartes = Organizaciones.objects.filter(sitio_accion__id=id_sitio)
    contrapartes = Organizaciones.objects.exclude(plataforma__id=8).order_by('nombre')
    if request.is_ajax():
        start = datetime.datetime.fromtimestamp(float(request.GET['start']))
        end = datetime.datetime.fromtimestamp(float(request.GET['end']))
        fecha1 = datetime.date(start.year, start.month, start.day)
        fecha2 = datetime.date(end.year, end.month, end.day)
        
        eventos = Agendas.objects.filter(inicio__range=(fecha1, fecha2),
                                        publico=True,
                                        sitio_accion__id=id_sitio)
        
        var = []        
        for evento in eventos:
            d = {
                 'id': str(evento.id),
                 'title': u'%s' % (evento.evento), 
                 'start':str(evento.inicio), 
                 'end':str(evento.final), 
                 'allDay': True,
                 'color':str(evento.user.userprofile.contraparte.font_color),
                 }
            var.append(d)
        return HttpResponse(simplejson.dumps(var), mimetype='application/json')

    #if not id==None:
    #    actividad = Agendas.objects.get(pk=id)
    
    return render_to_response('comunicacion/agendas/agenda_list_public.html',locals(),
                              context_instance = RequestContext(request))

@login_required
@csrf_exempt
def calendario_full_contraparte(request,id=None):
    paises = Pais.objects.all()
    contrapartes = Organizaciones.objects.all()
    if request.method == 'POST':
        request.session['p'] = request.POST.getlist('contraparte')
        
    if request.is_ajax():
        start = datetime.datetime.fromtimestamp(float(request.GET['start']))
        end = datetime.datetime.fromtimestamp(float(request.GET['end']))
        fecha1 = datetime.date(start.year, start.month, start.day)
        fecha2 = datetime.date(end.year, end.month, end.day)

        
        eventos = Agendas.objects.filter(inicio__range=(fecha1, fecha2),
                  user__userprofile__contraparte__id__in=request.session['p'])
        
        var = []        
        for evento in eventos:
            d = {
                 'id': str(evento.id),
                 'title': u'%s' % (evento.evento), 
                 'start':str(evento.inicio), 
                 'end':str(evento.final), 
                 'allDay': True,
                 'color':str(evento.user.userprofile.contraparte.font_color)
                 }
            var.append(d)
        return HttpResponse(simplejson.dumps(var), mimetype='application/json')
    if not id==None:
        actividad = Agendas.objects.get(pk=id)
    contrapartes_sel = Organizaciones.objects.filter(id__in=request.session['p'])
    contrapartes_otras = Organizaciones.objects.exclude(id__in=request.session['p'])
    return render_to_response('comunicacion/agendas/agenda_list_full.html',locals(),
                              context_instance = RequestContext(request))


#enviar mensajes cuando se crea un evento

def notify_all_event(eventos):
    site = Site.objects.get_current()
    users = User.objects.all() #.exclude(username=foros.contraparte.username)
    contenido = render_to_string('comunicacion/agendas/notify_new_event.txt', {'evento': eventos,
                                 'url': '%s/agendas/calendario/%s' % (site, eventos.id),
                                 #'url_aporte': '%s/foros/ver/%s/#aporte' % (site, foros.id),
                                 })
    send_mail('Nuevo evento en Alianza CAC', contenido, 'alianza.cac@gmail.com', [user.email for user in users if user.email])
   
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from mapeo.models import Persona

# Create your models here.
class Recolector(models.Model):
    ''' Esta es la clase para el nombre del recolector
    '''
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Recolector"

CHOICE_SEXO = ((1,'Hombre'),(2,'Mujer'))
CHOICE_OPCION = ((1,'Si'),(2,'No')) # Este choice se utilizara en toda la aplicacion que necesite si o no
CHOICE_RANGO = (
                (1, '18 - 25'),
                (2, '26 - 45'),
                (3, '26 - 65'),
                (4, 'Más de 65')
            )
CHOICE_NIVEL_EDUCATIVO = (
                (1, 'No sabe leer o escribir'),
                (2, 'Primaria Incompleta'),
                (3, 'Primaria Completa'),
                (4, 'Secundaria Incompleta'),
                (5, 'Bachiller'),
                (6, 'Universitario'),
            )

CHOICE_2_TIPOS = ((1,'Linea Base'),(2,'Entrevista Mujer'))

class Encuesta(models.Model):
    ''' Esta es la parte de la encuesta donde van los demas
    '''
    fecha = models.DateField()
    recolector = models.ForeignKey(Recolector)
    productor = models.ForeignKey(Persona, verbose_name='Entrevistado')
    jefe = models.IntegerField(choices=CHOICE_OPCION, verbose_name='Esta persona es jefe de la casa')
    tipo_encuesta = models.IntegerField(choices=CHOICE_2_TIPOS, default=2)


    user = models.ForeignKey(User)
    
    #campos ocultos para querys
    year = models.IntegerField(editable=False)
    
    def save(self):
        self.year = self.fecha.year
        super(Encuesta, self).save()
    
    def __unicode__(self):
        return self.productor.nombre
        
    class Meta:
        verbose_name_plural = "Encuesta"

## Indicador 1: Familia

CHOICE_EDUCACION = ((1,'Hombre mas de 18 años'),(2,'Mujeres mas de 18 años'),(3,'Hombre de 7 a 18 años'),
                     (4,'Mujeres de 7 a 18 años'),(5,'Niños menos de 6 años'),(6,'Niñas menos de 6 años'))

CHOICE_DESDE = ((1,'Menos de 5 años'),(2,'Más de 5 años'),(3,'No utilizar'))

##-------------------------------------------------------------------------------

# Indicador 3 y 4. Tipo de tenencia de parcela y solar y Documento legal de la propiedad, a nombre de quién

CHOICE_TENENCIA_1 = ((1,"Tierra propia (con o sin documento)"),(2,"Tierra mediaría"),
                   (3,"Tierra prestada"),(4,"Tierra colectiva"),
                   (5,"Tierra arrendada"),(6,"Tierra familiar"),(7,"Sin acceso a tierra"),)
                   
CHOICE_TENENCIA_2 = ((1,"Escritura pública"),(2,"Título de reforma Agraria"),
                   (3,"Promesa de venta"),(4,"Escritura posesoria"),
                   (5,"Testamento o Herencia"),(6,"Sin documento"),)
               
CHOICE_DUENO = ((1,"Hombre"),(2,"Mujer"),(3,"Mancomunado"),(4,"Parientes"),
                (5,"Colectivo"),(6,"No hay"))

class TenenciaFamilia(models.Model):
    nombre = models.CharField(max_length=250)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Opciones de acceso a tierra"

class TenenciaEntre(models.Model):
    nombre = models.CharField(max_length=250)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Opciones tenecia de tierra"

class OpcionesDueno(models.Model):
    nombre = models.CharField(max_length=250)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Opciones de documento de la tierra"

class Tenencia(models.Model):
    ''' Modelo tipo de tenencia de la propiedad
    '''
    parcela = models.ManyToManyField(TenenciaFamilia, verbose_name='Acceso a la tierra (Familia)')
    solar = models.ManyToManyField(TenenciaEntre, verbose_name='Tenencia de tierra familiar')
    dueno = models.ManyToManyField(OpcionesDueno, verbose_name='Documento de la tierra familiar a nombre de quién')
    encuesta = models.ForeignKey(Encuesta)
    
    #def __unicode__(self):
    #    return u'%s' % self.get_parcela_display()

    class Meta:
        verbose_name_plural = "Tenecia de la familia"

class TenenciaEntrevistada(models.Model):
    ''' Modelo tipo de tenencia de la propiedad
    '''
    parcela = models.ManyToManyField(TenenciaFamilia, verbose_name='Acceso a la tierra (de la persona entrevistada)')
    solar = models.ManyToManyField(TenenciaEntre, verbose_name='Tenencia de tierra de la persona entrevistada')
    dueno = models.ManyToManyField(OpcionesDueno, verbose_name='Documento de la tierra de la persona entrevistas a nombre de quién')
    encuesta = models.ForeignKey(Encuesta)
    
    #def __unicode__(self):
    #    return u'%s' % self.get_parcela_display()

    class Meta:
        verbose_name_plural = "Tenencia entrevistada"

#-----------------------------------------------------------
CHOICE_CASA_SOLAR = (
                    (1,"Propios (con o sin documento)"),
                    (2,"De su esposo/a"),
                    (3,"De su padres o suegros"),
                    (4,"Compartidos con los padres o suegros"),
                    (5,"Compartidos con familiares"),
                    (6,"Compartidos con otra familia"),
                    (7,"Alquilados"),
                )
CHOICE_TENENCIA_SOLAR = (
                    (1,"Escritura pública"),
                    (2,"Promesa de venta"),
                    (3,"Testamento o Herencia"),
                    (4,"Título de reforma Agraria"),
                    (5,"Escritura posesoria"),
                    (6,"Sin documento"),
                    (7,"No aplica"),
                )
CHOICE_DUENO_CASA_SOLAR = ((1,"Hombre"),(2,"Mujer"),(3,"Mancomunado"))

class CasaSolar(models.Model):
    casa = models.IntegerField('La casa y el solar son', choices=CHOICE_CASA_SOLAR)
    tenencia = models.IntegerField('Tenencia de solar', choices=CHOICE_TENENCIA_SOLAR)
    dueno = models.IntegerField('Documento legal de la propiedad, a nombre de quien', choices=CHOICE_DUENO_CASA_SOLAR)
    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = "Casa y solar"
    
#-------------------------------------------------------------------------------


CHOICE_MANEJA = ((1,"Hombre"),(2,"Mujer"),(3,"Ambos"),(4,"Hijos/as"),
                 (5,'Hombre-Hijos'),(6,'Mujer-Hijos'),(7,'Todos'))

#-------------------------------------------------------------------------------

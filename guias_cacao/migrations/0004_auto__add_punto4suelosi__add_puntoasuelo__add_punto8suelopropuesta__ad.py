# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Punto4SueloSI'
        db.create_table(u'guias_cacao_punto4suelosi', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('opcion', self.gf('django.db.models.fields.IntegerField')()),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guias_cacao.FichaSuelo'])),
        ))
        db.send_create_signal(u'guias_cacao', ['Punto4SueloSI'])

        # Adding model 'PuntoASuelo'
        db.create_table(u'guias_cacao_puntoasuelo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('opcion', self.gf('django.db.models.fields.IntegerField')()),
            ('respuesta', self.gf('django.db.models.fields.IntegerField')()),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guias_cacao.FichaSuelo'])),
        ))
        db.send_create_signal(u'guias_cacao', ['PuntoASuelo'])

        # Adding model 'Punto8SueloPropuesta'
        db.create_table(u'guias_cacao_punto8suelopropuesta', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guias_cacao.TipoFertilizantes'])),
            ('cantidad', self.gf('django.db.models.fields.FloatField')()),
            ('unidad', self.gf('django.db.models.fields.IntegerField')()),
            ('frecuencia', self.gf('django.db.models.fields.FloatField')()),
            ('meses', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=23)),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guias_cacao.FichaSuelo'])),
        ))
        db.send_create_signal(u'guias_cacao', ['Punto8SueloPropuesta'])

        # Adding model 'Punto9Enfermedades'
        db.create_table(u'guias_cacao_punto9enfermedades', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('limitaciones', self.gf('django.db.models.fields.IntegerField')()),
            ('acciones', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=5)),
            ('donde', self.gf('django.db.models.fields.IntegerField')()),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guias_cacao.FichaSuelo'])),
        ))
        db.send_create_signal(u'guias_cacao', ['Punto9Enfermedades'])

        # Adding model 'Punto9Desbalance'
        db.create_table(u'guias_cacao_punto9desbalance', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('limitaciones', self.gf('django.db.models.fields.IntegerField')()),
            ('acciones', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=1)),
            ('donde', self.gf('django.db.models.fields.IntegerField')()),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guias_cacao.FichaSuelo'])),
        ))
        db.send_create_signal(u'guias_cacao', ['Punto9Desbalance'])

        # Adding model 'Punto9Drenaje'
        db.create_table(u'guias_cacao_punto9drenaje', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('limitaciones', self.gf('django.db.models.fields.IntegerField')()),
            ('acciones', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=5)),
            ('donde', self.gf('django.db.models.fields.IntegerField')()),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guias_cacao.FichaSuelo'])),
        ))
        db.send_create_signal(u'guias_cacao', ['Punto9Drenaje'])

        # Adding model 'Punto4Suelo'
        db.create_table(u'guias_cacao_punto4suelo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('area', self.gf('django.db.models.fields.FloatField')()),
            ('densidad', self.gf('django.db.models.fields.FloatField')()),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guias_cacao.FichaSuelo'])),
        ))
        db.send_create_signal(u'guias_cacao', ['Punto4Suelo'])

        # Adding model 'Punto9Exceso'
        db.create_table(u'guias_cacao_punto9exceso', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('limitaciones', self.gf('django.db.models.fields.IntegerField')()),
            ('acciones', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=1)),
            ('donde', self.gf('django.db.models.fields.IntegerField')()),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guias_cacao.FichaSuelo'])),
        ))
        db.send_create_signal(u'guias_cacao', ['Punto9Exceso'])

        # Adding model 'TipoFertilizantes'
        db.create_table(u'guias_cacao_tipofertilizantes', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'guias_cacao', ['TipoFertilizantes'])

        # Adding model 'Punto2BSuelo'
        db.create_table(u'guias_cacao_punto2bsuelo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('opcion', self.gf('django.db.models.fields.IntegerField')()),
            ('respuesta', self.gf('django.db.models.fields.IntegerField')()),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guias_cacao.FichaSuelo'])),
        ))
        db.send_create_signal(u'guias_cacao', ['Punto2BSuelo'])

        # Adding model 'PuntoBSuelo'
        db.create_table(u'guias_cacao_puntobsuelo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('opcion', self.gf('django.db.models.fields.IntegerField')()),
            ('respuesta', self.gf('django.db.models.fields.IntegerField')()),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guias_cacao.FichaSuelo'])),
        ))
        db.send_create_signal(u'guias_cacao', ['PuntoBSuelo'])

        # Adding model 'Punto6AnalisisSuelo'
        db.create_table(u'guias_cacao_punto6analisissuelo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('variable', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guias_cacao.DatosAnalisis'])),
            ('valor', self.gf('django.db.models.fields.FloatField')()),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guias_cacao.FichaSuelo'])),
        ))
        db.send_create_signal(u'guias_cacao', ['Punto6AnalisisSuelo'])

        # Adding model 'Punto1Suelo'
        db.create_table(u'guias_cacao_punto1suelo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uso_parcela', self.gf('django.db.models.fields.IntegerField')()),
            ('limitante', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=15)),
            ('orientacion', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=13)),
            ('abonos', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=11)),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guias_cacao.FichaSuelo'])),
        ))
        db.send_create_signal(u'guias_cacao', ['Punto1Suelo'])

        # Adding model 'Punto2ASuelo'
        db.create_table(u'guias_cacao_punto2asuelo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('opcion', self.gf('django.db.models.fields.IntegerField')()),
            ('respuesta', self.gf('django.db.models.fields.IntegerField')()),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guias_cacao.FichaSuelo'])),
        ))
        db.send_create_signal(u'guias_cacao', ['Punto2ASuelo'])

        # Adding model 'Punto9Nutrientes'
        db.create_table(u'guias_cacao_punto9nutrientes', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('limitaciones', self.gf('django.db.models.fields.IntegerField')()),
            ('acciones', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=3)),
            ('donde', self.gf('django.db.models.fields.IntegerField')()),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guias_cacao.FichaSuelo'])),
        ))
        db.send_create_signal(u'guias_cacao', ['Punto9Nutrientes'])

        # Adding model 'Punto3SueloPunto3'
        db.create_table(u'guias_cacao_punto3suelopunto3', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('opcion', self.gf('django.db.models.fields.IntegerField')()),
            ('respuesta', self.gf('django.db.models.fields.IntegerField')()),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guias_cacao.FichaSuelo'])),
        ))
        db.send_create_signal(u'guias_cacao', ['Punto3SueloPunto3'])

        # Adding model 'Punto3SueloPunto2'
        db.create_table(u'guias_cacao_punto3suelopunto2', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('opcion', self.gf('django.db.models.fields.IntegerField')()),
            ('respuesta', self.gf('django.db.models.fields.IntegerField')()),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guias_cacao.FichaSuelo'])),
        ))
        db.send_create_signal(u'guias_cacao', ['Punto3SueloPunto2'])

        # Adding model 'Punto3SueloPunto1'
        db.create_table(u'guias_cacao_punto3suelopunto1', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('opcion', self.gf('django.db.models.fields.IntegerField')()),
            ('respuesta', self.gf('django.db.models.fields.IntegerField')()),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guias_cacao.FichaSuelo'])),
        ))
        db.send_create_signal(u'guias_cacao', ['Punto3SueloPunto1'])

        # Adding model 'Punto4SueloCosecha'
        db.create_table(u'guias_cacao_punto4suelocosecha', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('producto', self.gf('django.db.models.fields.IntegerField')()),
            ('cantidad', self.gf('django.db.models.fields.FloatField')()),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guias_cacao.FichaSuelo'])),
        ))
        db.send_create_signal(u'guias_cacao', ['Punto4SueloCosecha'])

        # Adding model 'Punto5SueloAbonos'
        db.create_table(u'guias_cacao_punto5sueloabonos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guias_cacao.TipoFertilizantes'])),
            ('cantidad', self.gf('django.db.models.fields.FloatField')()),
            ('unidad', self.gf('django.db.models.fields.IntegerField')()),
            ('humedad', self.gf('django.db.models.fields.FloatField')()),
            ('frecuencia', self.gf('django.db.models.fields.FloatField')()),
            ('meses', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=23)),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guias_cacao.FichaSuelo'])),
        ))
        db.send_create_signal(u'guias_cacao', ['Punto5SueloAbonos'])

        # Adding model 'Punto9Erosion'
        db.create_table(u'guias_cacao_punto9erosion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('limitaciones', self.gf('django.db.models.fields.IntegerField')()),
            ('acciones', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=9)),
            ('donde', self.gf('django.db.models.fields.IntegerField')()),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guias_cacao.FichaSuelo'])),
        ))
        db.send_create_signal(u'guias_cacao', ['Punto9Erosion'])

        # Adding model 'Punto7TipoSuelo'
        db.create_table(u'guias_cacao_punto7tiposuelo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('opcion', self.gf('django.db.models.fields.IntegerField')()),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guias_cacao.FichaSuelo'])),
        ))
        db.send_create_signal(u'guias_cacao', ['Punto7TipoSuelo'])

        # Adding model 'FichaSuelo'
        db.create_table(u'guias_cacao_fichasuelo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('productor', self.gf('django.db.models.fields.related.ForeignKey')(related_name='persona_productor_suelo', to=orm['mapeo.Persona'])),
            ('tecnico', self.gf('django.db.models.fields.related.ForeignKey')(related_name='persona_tecnico_suelo', to=orm['mapeo.Persona'])),
            ('fecha_visita', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'guias_cacao', ['FichaSuelo'])

        # Adding model 'DatosAnalisis'
        db.create_table(u'guias_cacao_datosanalisis', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('variable', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('unidad', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('valor_critico', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'guias_cacao', ['DatosAnalisis'])


    def backwards(self, orm):
        # Deleting model 'Punto4SueloSI'
        db.delete_table(u'guias_cacao_punto4suelosi')

        # Deleting model 'PuntoASuelo'
        db.delete_table(u'guias_cacao_puntoasuelo')

        # Deleting model 'Punto8SueloPropuesta'
        db.delete_table(u'guias_cacao_punto8suelopropuesta')

        # Deleting model 'Punto9Enfermedades'
        db.delete_table(u'guias_cacao_punto9enfermedades')

        # Deleting model 'Punto9Desbalance'
        db.delete_table(u'guias_cacao_punto9desbalance')

        # Deleting model 'Punto9Drenaje'
        db.delete_table(u'guias_cacao_punto9drenaje')

        # Deleting model 'Punto4Suelo'
        db.delete_table(u'guias_cacao_punto4suelo')

        # Deleting model 'Punto9Exceso'
        db.delete_table(u'guias_cacao_punto9exceso')

        # Deleting model 'TipoFertilizantes'
        db.delete_table(u'guias_cacao_tipofertilizantes')

        # Deleting model 'Punto2BSuelo'
        db.delete_table(u'guias_cacao_punto2bsuelo')

        # Deleting model 'PuntoBSuelo'
        db.delete_table(u'guias_cacao_puntobsuelo')

        # Deleting model 'Punto6AnalisisSuelo'
        db.delete_table(u'guias_cacao_punto6analisissuelo')

        # Deleting model 'Punto1Suelo'
        db.delete_table(u'guias_cacao_punto1suelo')

        # Deleting model 'Punto2ASuelo'
        db.delete_table(u'guias_cacao_punto2asuelo')

        # Deleting model 'Punto9Nutrientes'
        db.delete_table(u'guias_cacao_punto9nutrientes')

        # Deleting model 'Punto3SueloPunto3'
        db.delete_table(u'guias_cacao_punto3suelopunto3')

        # Deleting model 'Punto3SueloPunto2'
        db.delete_table(u'guias_cacao_punto3suelopunto2')

        # Deleting model 'Punto3SueloPunto1'
        db.delete_table(u'guias_cacao_punto3suelopunto1')

        # Deleting model 'Punto4SueloCosecha'
        db.delete_table(u'guias_cacao_punto4suelocosecha')

        # Deleting model 'Punto5SueloAbonos'
        db.delete_table(u'guias_cacao_punto5sueloabonos')

        # Deleting model 'Punto9Erosion'
        db.delete_table(u'guias_cacao_punto9erosion')

        # Deleting model 'Punto7TipoSuelo'
        db.delete_table(u'guias_cacao_punto7tiposuelo')

        # Deleting model 'FichaSuelo'
        db.delete_table(u'guias_cacao_fichasuelo')

        # Deleting model 'DatosAnalisis'
        db.delete_table(u'guias_cacao_datosanalisis')


    models = {
        u'guias_cacao.accionesenfermedad': {
            'Meta': {'object_name': 'AccionesEnfermedad'},
            'cuantas_veces': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPlaga']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meses': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '23'}),
            'plagas_acciones': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'realiza_manejo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'guias_cacao.accionessombra': {
            'Meta': {'object_name': 'AccionesSombra'},
            'accion': ('django.db.models.fields.IntegerField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSombra']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.analisispoda': {
            'Meta': {'object_name': 'AnalisisPoda'},
            'campo1': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '15'}),
            'campo2': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'}),
            'campo3': ('django.db.models.fields.IntegerField', [], {}),
            'campo4': ('django.db.models.fields.IntegerField', [], {}),
            'campo5': ('django.db.models.fields.IntegerField', [], {}),
            'campo6': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '23'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPoda']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.analisissombra': {
            'Meta': {'object_name': 'AnalisisSombra'},
            'Problema': ('django.db.models.fields.IntegerField', [], {}),
            'arreglo': ('django.db.models.fields.IntegerField', [], {}),
            'calidad_hojarasca': ('django.db.models.fields.IntegerField', [], {}),
            'competencia': ('django.db.models.fields.IntegerField', [], {}),
            'densidad': ('django.db.models.fields.IntegerField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSombra']"}),
            'forma_copa': ('django.db.models.fields.IntegerField', [], {}),
            'hojarasca': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.aumentarsombra': {
            'Meta': {'object_name': 'AumentarSombra'},
            'cambiando': ('django.db.models.fields.IntegerField', [], {}),
            'cambiando_cuales': ('django.db.models.fields.CharField', [], {'max_length': '350'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSombra']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'que_parte': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'sembrando': ('django.db.models.fields.IntegerField', [], {}),
            'sembrando_cuales': ('django.db.models.fields.CharField', [], {'max_length': '350'}),
            'todo': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.cobertura1': {
            'Meta': {'object_name': 'Cobertura1'},
            'cobertura': ('django.db.models.fields.FloatField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSombra']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.cobertura2': {
            'Meta': {'object_name': 'Cobertura2'},
            'cobertura': ('django.db.models.fields.FloatField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSombra']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.cobertura3': {
            'Meta': {'object_name': 'Cobertura3'},
            'cobertura': ('django.db.models.fields.FloatField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSombra']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.datosanalisis': {
            'Meta': {'object_name': 'DatosAnalisis'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'unidad': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'valor_critico': ('django.db.models.fields.FloatField', [], {}),
            'variable': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'guias_cacao.especies': {
            'Meta': {'object_name': 'Especies'},
            'foto': (u'sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'g_altura': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'g_ancho': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'g_diametro': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'm_altura': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'm_ancho': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'm_diametro': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'nombre_cientifico': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'p_altura': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'p_ancho': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'p_diametro': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tipo_uso': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'})
        },
        u'guias_cacao.fichapiso': {
            'Meta': {'object_name': 'FichaPiso'},
            'fecha_visita': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'productor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'persona_productor_piso'", 'to': u"orm['mapeo.Persona']"}),
            'tecnico': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'persona_tecnico_piso'", 'to': u"orm['mapeo.Persona']"})
        },
        u'guias_cacao.fichaplaga': {
            'Meta': {'object_name': 'FichaPlaga'},
            'fecha_visita': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'productor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'persona_productor_plaga'", 'to': u"orm['mapeo.Persona']"}),
            'tecnico': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'persona_tecnico_plaga'", 'to': u"orm['mapeo.Persona']"})
        },
        u'guias_cacao.fichapoda': {
            'Meta': {'object_name': 'FichaPoda'},
            'fecha_visita': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'productor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'setproductor'", 'to': u"orm['mapeo.Persona']"}),
            'tecnico': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'settecnico'", 'to': u"orm['mapeo.Persona']"})
        },
        u'guias_cacao.fichasombra': {
            'Meta': {'object_name': 'FichaSombra'},
            'fecha_visita': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'productor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'persona_productor'", 'to': u"orm['mapeo.Persona']"}),
            'tecnico': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'persona_tecnico'", 'to': u"orm['mapeo.Persona']"})
        },
        u'guias_cacao.fichasuelo': {
            'Meta': {'object_name': 'FichaSuelo'},
            'fecha_visita': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'productor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'persona_productor_suelo'", 'to': u"orm['mapeo.Persona']"}),
            'tecnico': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'persona_tecnico_suelo'", 'to': u"orm['mapeo.Persona']"})
        },
        u'guias_cacao.foto1': {
            'Meta': {'object_name': 'Foto1'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSombra']"}),
            'foto': (u'sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.foto2': {
            'Meta': {'object_name': 'Foto2'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSombra']"}),
            'foto': (u'sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.foto3': {
            'Meta': {'object_name': 'Foto3'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSombra']"}),
            'foto': (u'sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.manejopoda': {
            'Meta': {'object_name': 'ManejoPoda'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPoda']"}),
            'formacion': ('django.db.models.fields.IntegerField', [], {}),
            'herramientas': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.manejosombra': {
            'Meta': {'object_name': 'ManejoSombra'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSombra']"}),
            'formacion': ('django.db.models.fields.IntegerField', [], {}),
            'herramientas': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.observacionpunto1': {
            'Meta': {'object_name': 'ObservacionPunto1'},
            'cinco': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cuatro': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dies': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dos': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPlaga']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nueve': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ocho': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'planta': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'seis': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'siete': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tres': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'uno': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'guias_cacao.observacionpunto1nivel': {
            'Meta': {'object_name': 'ObservacionPunto1Nivel'},
            'cinco': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cuatro': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dies': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dos': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPlaga']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nueve': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ocho': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'planta': ('django.db.models.fields.IntegerField', [], {}),
            'seis': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'siete': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tres': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'uno': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'guias_cacao.observacionpunto2': {
            'Meta': {'object_name': 'ObservacionPunto2'},
            'cinco': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cuatro': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dies': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dos': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPlaga']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nueve': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ocho': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'planta': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'seis': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'siete': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tres': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'uno': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'guias_cacao.observacionpunto2nivel': {
            'Meta': {'object_name': 'ObservacionPunto2Nivel'},
            'cinco': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cuatro': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dies': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dos': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPlaga']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nueve': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ocho': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'planta': ('django.db.models.fields.IntegerField', [], {}),
            'seis': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'siete': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tres': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'uno': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'guias_cacao.observacionpunto3': {
            'Meta': {'object_name': 'ObservacionPunto3'},
            'cinco': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cuatro': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dies': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dos': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPlaga']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nueve': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ocho': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'planta': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'seis': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'siete': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tres': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'uno': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'guias_cacao.observacionpunto3nivel': {
            'Meta': {'object_name': 'ObservacionPunto3Nivel'},
            'cinco': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cuatro': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dies': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dos': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPlaga']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nueve': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ocho': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'planta': ('django.db.models.fields.IntegerField', [], {}),
            'seis': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'siete': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tres': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'uno': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'guias_cacao.orientacion': {
            'Meta': {'object_name': 'Orientacion'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPlaga']"}),
            'fuentes': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.pisopunto1': {
            'Meta': {'object_name': 'PisoPunto1'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPiso']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'punto1': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '13'}),
            'punto2': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '13'})
        },
        u'guias_cacao.pisopunto10': {
            'Meta': {'object_name': 'PisoPunto10'},
            'equipo': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '15'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPiso']"}),
            'formacion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.pisopunto3': {
            'Meta': {'object_name': 'PisoPunto3'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPiso']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manejo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'meses': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '23'}),
            'realiza': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'veces': ('django.db.models.fields.FloatField', [], {})
        },
        u'guias_cacao.pisopunto4': {
            'Meta': {'object_name': 'PisoPunto4'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPiso']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manejo': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'})
        },
        u'guias_cacao.pisopunto5': {
            'Meta': {'object_name': 'PisoPunto5'},
            'conteo': ('django.db.models.fields.FloatField', [], {}),
            'estado': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPiso']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.pisopunto6': {
            'Meta': {'object_name': 'PisoPunto6'},
            'estado': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPiso']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maleza': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'}),
            'manejo': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '5'})
        },
        u'guias_cacao.pisopunto7': {
            'Meta': {'object_name': 'PisoPunto7'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPiso']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manejo': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'}),
            'sombra': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '7'}),
            'suelo': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'})
        },
        u'guias_cacao.pisopunto8': {
            'Meta': {'object_name': 'PisoPunto8'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPiso']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meses': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '23'}),
            'parte': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'piso': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'guias_cacao.plagasenfermedad': {
            'Meta': {'object_name': 'PlagasEnfermedad'},
            'dano': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPlaga']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'plagas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'promedio': ('django.db.models.fields.FloatField', [], {}),
            'visto': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'guias_cacao.problemasprincipales': {
            'Meta': {'object_name': 'ProblemasPrincipales'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPlaga']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'observadas': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '27'}),
            'principales': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '27'}),
            'situacion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'guias_cacao.punto1': {
            'Meta': {'object_name': 'Punto1'},
            'especie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.Especies']"}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSombra']"}),
            'grande': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mediana': ('django.db.models.fields.FloatField', [], {}),
            'pequena': ('django.db.models.fields.FloatField', [], {}),
            'tipo': ('django.db.models.fields.IntegerField', [], {}),
            'tipo_de_copa': ('django.db.models.fields.IntegerField', [], {}),
            'uso': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto1a': {
            'Meta': {'object_name': 'Punto1A'},
            'cinco': ('django.db.models.fields.FloatField', [], {}),
            'cuatro': ('django.db.models.fields.FloatField', [], {}),
            'diez': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dos': ('django.db.models.fields.FloatField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPoda']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nueve': ('django.db.models.fields.FloatField', [], {}),
            'ocho': ('django.db.models.fields.FloatField', [], {}),
            'plantas': ('django.db.models.fields.IntegerField', [], {}),
            'seis': ('django.db.models.fields.FloatField', [], {}),
            'siete': ('django.db.models.fields.FloatField', [], {}),
            'tres': ('django.db.models.fields.FloatField', [], {}),
            'uno': ('django.db.models.fields.FloatField', [], {})
        },
        u'guias_cacao.punto1b': {
            'Meta': {'object_name': 'Punto1B'},
            'cinco': ('django.db.models.fields.IntegerField', [], {}),
            'cuatro': ('django.db.models.fields.IntegerField', [], {}),
            'diez': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dos': ('django.db.models.fields.IntegerField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPoda']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nueve': ('django.db.models.fields.IntegerField', [], {}),
            'ocho': ('django.db.models.fields.IntegerField', [], {}),
            'plantas': ('django.db.models.fields.IntegerField', [], {}),
            'seis': ('django.db.models.fields.IntegerField', [], {}),
            'siete': ('django.db.models.fields.IntegerField', [], {}),
            'tres': ('django.db.models.fields.IntegerField', [], {}),
            'uno': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto1c': {
            'Meta': {'object_name': 'Punto1C'},
            'cinco': ('django.db.models.fields.IntegerField', [], {}),
            'cuatro': ('django.db.models.fields.IntegerField', [], {}),
            'diez': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dos': ('django.db.models.fields.IntegerField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPoda']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nueve': ('django.db.models.fields.IntegerField', [], {}),
            'ocho': ('django.db.models.fields.IntegerField', [], {}),
            'plantas': ('django.db.models.fields.IntegerField', [], {}),
            'seis': ('django.db.models.fields.IntegerField', [], {}),
            'siete': ('django.db.models.fields.IntegerField', [], {}),
            'tres': ('django.db.models.fields.IntegerField', [], {}),
            'uno': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto1suelo': {
            'Meta': {'object_name': 'Punto1Suelo'},
            'abonos': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSuelo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'limitante': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '15'}),
            'orientacion': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '13'}),
            'uso_parcela': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto2': {
            'Meta': {'object_name': 'Punto2'},
            'especie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.Especies']"}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSombra']"}),
            'grande': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mediana': ('django.db.models.fields.FloatField', [], {}),
            'pequena': ('django.db.models.fields.FloatField', [], {}),
            'tipo': ('django.db.models.fields.IntegerField', [], {}),
            'tipo_de_copa': ('django.db.models.fields.IntegerField', [], {}),
            'uso': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto2a': {
            'Meta': {'object_name': 'Punto2A'},
            'cinco': ('django.db.models.fields.FloatField', [], {}),
            'cuatro': ('django.db.models.fields.FloatField', [], {}),
            'diez': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dos': ('django.db.models.fields.FloatField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPoda']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nueve': ('django.db.models.fields.FloatField', [], {}),
            'ocho': ('django.db.models.fields.FloatField', [], {}),
            'plantas': ('django.db.models.fields.IntegerField', [], {}),
            'seis': ('django.db.models.fields.FloatField', [], {}),
            'siete': ('django.db.models.fields.FloatField', [], {}),
            'tres': ('django.db.models.fields.FloatField', [], {}),
            'uno': ('django.db.models.fields.FloatField', [], {})
        },
        u'guias_cacao.punto2asuelo': {
            'Meta': {'object_name': 'Punto2ASuelo'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSuelo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'opcion': ('django.db.models.fields.IntegerField', [], {}),
            'respuesta': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto2b': {
            'Meta': {'object_name': 'Punto2B'},
            'cinco': ('django.db.models.fields.IntegerField', [], {}),
            'cuatro': ('django.db.models.fields.IntegerField', [], {}),
            'diez': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dos': ('django.db.models.fields.IntegerField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPoda']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nueve': ('django.db.models.fields.IntegerField', [], {}),
            'ocho': ('django.db.models.fields.IntegerField', [], {}),
            'plantas': ('django.db.models.fields.IntegerField', [], {}),
            'seis': ('django.db.models.fields.IntegerField', [], {}),
            'siete': ('django.db.models.fields.IntegerField', [], {}),
            'tres': ('django.db.models.fields.IntegerField', [], {}),
            'uno': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto2bsuelo': {
            'Meta': {'object_name': 'Punto2BSuelo'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSuelo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'opcion': ('django.db.models.fields.IntegerField', [], {}),
            'respuesta': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto2c': {
            'Meta': {'object_name': 'Punto2C'},
            'cinco': ('django.db.models.fields.IntegerField', [], {}),
            'cuatro': ('django.db.models.fields.IntegerField', [], {}),
            'diez': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dos': ('django.db.models.fields.IntegerField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPoda']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nueve': ('django.db.models.fields.IntegerField', [], {}),
            'ocho': ('django.db.models.fields.IntegerField', [], {}),
            'plantas': ('django.db.models.fields.IntegerField', [], {}),
            'seis': ('django.db.models.fields.IntegerField', [], {}),
            'siete': ('django.db.models.fields.IntegerField', [], {}),
            'tres': ('django.db.models.fields.IntegerField', [], {}),
            'uno': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto3': {
            'Meta': {'object_name': 'Punto3'},
            'especie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.Especies']"}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSombra']"}),
            'grande': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mediana': ('django.db.models.fields.FloatField', [], {}),
            'pequena': ('django.db.models.fields.FloatField', [], {}),
            'tipo': ('django.db.models.fields.IntegerField', [], {}),
            'tipo_de_copa': ('django.db.models.fields.IntegerField', [], {}),
            'uso': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto3a': {
            'Meta': {'object_name': 'Punto3A'},
            'cinco': ('django.db.models.fields.FloatField', [], {}),
            'cuatro': ('django.db.models.fields.FloatField', [], {}),
            'diez': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dos': ('django.db.models.fields.FloatField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPoda']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nueve': ('django.db.models.fields.FloatField', [], {}),
            'ocho': ('django.db.models.fields.FloatField', [], {}),
            'plantas': ('django.db.models.fields.IntegerField', [], {}),
            'seis': ('django.db.models.fields.FloatField', [], {}),
            'siete': ('django.db.models.fields.FloatField', [], {}),
            'tres': ('django.db.models.fields.FloatField', [], {}),
            'uno': ('django.db.models.fields.FloatField', [], {})
        },
        u'guias_cacao.punto3b': {
            'Meta': {'object_name': 'Punto3B'},
            'cinco': ('django.db.models.fields.IntegerField', [], {}),
            'cuatro': ('django.db.models.fields.IntegerField', [], {}),
            'diez': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dos': ('django.db.models.fields.IntegerField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPoda']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nueve': ('django.db.models.fields.IntegerField', [], {}),
            'ocho': ('django.db.models.fields.IntegerField', [], {}),
            'plantas': ('django.db.models.fields.IntegerField', [], {}),
            'seis': ('django.db.models.fields.IntegerField', [], {}),
            'siete': ('django.db.models.fields.IntegerField', [], {}),
            'tres': ('django.db.models.fields.IntegerField', [], {}),
            'uno': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto3c': {
            'Meta': {'object_name': 'Punto3C'},
            'cinco': ('django.db.models.fields.IntegerField', [], {}),
            'cuatro': ('django.db.models.fields.IntegerField', [], {}),
            'diez': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dos': ('django.db.models.fields.IntegerField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPoda']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nueve': ('django.db.models.fields.IntegerField', [], {}),
            'ocho': ('django.db.models.fields.IntegerField', [], {}),
            'plantas': ('django.db.models.fields.IntegerField', [], {}),
            'seis': ('django.db.models.fields.IntegerField', [], {}),
            'siete': ('django.db.models.fields.IntegerField', [], {}),
            'tres': ('django.db.models.fields.IntegerField', [], {}),
            'uno': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto3suelopunto1': {
            'Meta': {'object_name': 'Punto3SueloPunto1'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSuelo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'opcion': ('django.db.models.fields.IntegerField', [], {}),
            'respuesta': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto3suelopunto2': {
            'Meta': {'object_name': 'Punto3SueloPunto2'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSuelo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'opcion': ('django.db.models.fields.IntegerField', [], {}),
            'respuesta': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto3suelopunto3': {
            'Meta': {'object_name': 'Punto3SueloPunto3'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSuelo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'opcion': ('django.db.models.fields.IntegerField', [], {}),
            'respuesta': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto4suelo': {
            'Meta': {'object_name': 'Punto4Suelo'},
            'area': ('django.db.models.fields.FloatField', [], {}),
            'densidad': ('django.db.models.fields.FloatField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSuelo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.punto4suelocosecha': {
            'Meta': {'object_name': 'Punto4SueloCosecha'},
            'cantidad': ('django.db.models.fields.FloatField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSuelo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'producto': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto4suelosi': {
            'Meta': {'object_name': 'Punto4SueloSI'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSuelo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'opcion': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto5sueloabonos': {
            'Meta': {'object_name': 'Punto5SueloAbonos'},
            'cantidad': ('django.db.models.fields.FloatField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSuelo']"}),
            'frecuencia': ('django.db.models.fields.FloatField', [], {}),
            'humedad': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meses': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '23'}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.TipoFertilizantes']"}),
            'unidad': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto6analisissuelo': {
            'Meta': {'object_name': 'Punto6AnalisisSuelo'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSuelo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'valor': ('django.db.models.fields.FloatField', [], {}),
            'variable': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.DatosAnalisis']"})
        },
        u'guias_cacao.punto6plagas': {
            'Meta': {'object_name': 'Punto6Plagas'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPlaga']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manejo': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '15'}),
            'observaciones': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '15'}),
            'sombra': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'guias_cacao.punto7plagas': {
            'Meta': {'object_name': 'Punto7Plagas'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPlaga']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manejo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'meses': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '23'}),
            'parte': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'guias_cacao.punto7tiposuelo': {
            'Meta': {'object_name': 'Punto7TipoSuelo'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSuelo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'opcion': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto8suelopropuesta': {
            'Meta': {'object_name': 'Punto8SueloPropuesta'},
            'cantidad': ('django.db.models.fields.FloatField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSuelo']"}),
            'frecuencia': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meses': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '23'}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.TipoFertilizantes']"}),
            'unidad': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto8y9plagas': {
            'Meta': {'object_name': 'Punto8y9Plagas'},
            'equipos': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '15'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPlaga']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'opcion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'guias_cacao.punto9desbalance': {
            'Meta': {'object_name': 'Punto9Desbalance'},
            'acciones': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '1'}),
            'donde': ('django.db.models.fields.IntegerField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSuelo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'limitaciones': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto9drenaje': {
            'Meta': {'object_name': 'Punto9Drenaje'},
            'acciones': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '5'}),
            'donde': ('django.db.models.fields.IntegerField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSuelo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'limitaciones': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto9enfermedades': {
            'Meta': {'object_name': 'Punto9Enfermedades'},
            'acciones': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '5'}),
            'donde': ('django.db.models.fields.IntegerField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSuelo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'limitaciones': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto9erosion': {
            'Meta': {'object_name': 'Punto9Erosion'},
            'acciones': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '9'}),
            'donde': ('django.db.models.fields.IntegerField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSuelo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'limitaciones': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto9exceso': {
            'Meta': {'object_name': 'Punto9Exceso'},
            'acciones': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '1'}),
            'donde': ('django.db.models.fields.IntegerField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSuelo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'limitaciones': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto9nutrientes': {
            'Meta': {'object_name': 'Punto9Nutrientes'},
            'acciones': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '3'}),
            'donde': ('django.db.models.fields.IntegerField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSuelo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'limitaciones': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.puntoasuelo': {
            'Meta': {'object_name': 'PuntoASuelo'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSuelo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'opcion': ('django.db.models.fields.IntegerField', [], {}),
            'respuesta': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.puntobsuelo': {
            'Meta': {'object_name': 'PuntoBSuelo'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSuelo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'opcion': ('django.db.models.fields.IntegerField', [], {}),
            'respuesta': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.reducirsombra': {
            'Meta': {'object_name': 'ReducirSombra'},
            'eliminando': ('django.db.models.fields.IntegerField', [], {}),
            'eliminando_cuales': ('django.db.models.fields.CharField', [], {'max_length': '350'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSombra']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'poda': ('django.db.models.fields.IntegerField', [], {}),
            'poda_cuales': ('django.db.models.fields.CharField', [], {'max_length': '350'}),
            'que_parte': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'todo': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.tipofertilizantes': {
            'Meta': {'object_name': 'TipoFertilizantes'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'lugar.comunidad': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Comunidad'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'lugar.departamento': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Departamento'},
            'extension': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lugar.Pais']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True'})
        },
        u'lugar.municipio': {
            'Meta': {'ordering': "['departamento__nombre', 'nombre']", 'object_name': 'Municipio'},
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lugar.Departamento']"}),
            'extension': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True'})
        },
        u'lugar.pais': {
            'Meta': {'object_name': 'Pais'},
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'mapeo.persona': {
            'Meta': {'object_name': 'Persona'},
            'cedula': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'comunidad': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['lugar.Comunidad']"}),
            'departamento': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['lugar.Departamento']"}),
            'edad': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lugar.Pais']"}),
            'sexo': ('django.db.models.fields.IntegerField', [], {}),
            'tipo_persona': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['guias_cacao']
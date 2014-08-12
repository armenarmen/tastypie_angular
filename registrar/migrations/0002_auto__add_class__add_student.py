# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Class'
        db.create_table(u'registrar_class', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'registrar', ['Class'])

        # Adding model 'Student'
        db.create_table(u'registrar_student', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('klass', self.gf('django.db.models.fields.related.ForeignKey')(related_name='students', to=orm['registrar.Class'])),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'registrar', ['Student'])


    def backwards(self, orm):
        # Deleting model 'Class'
        db.delete_table(u'registrar_class')

        # Deleting model 'Student'
        db.delete_table(u'registrar_student')


    models = {
        u'registrar.class': {
            'Meta': {'object_name': 'Class'},
            'end_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '75'})
        },
        u'registrar.student': {
            'Meta': {'object_name': 'Student'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'klass': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'students'", 'to': u"orm['registrar.Class']"}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['registrar']
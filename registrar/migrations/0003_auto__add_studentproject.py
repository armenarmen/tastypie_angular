# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'StudentProject'
        db.create_table(u'registrar_studentproject', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registrar.Student'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'registrar', ['StudentProject'])


    def backwards(self, orm):
        # Deleting model 'StudentProject'
        db.delete_table(u'registrar_studentproject')


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
        },
        u'registrar.studentproject': {
            'Meta': {'object_name': 'StudentProject'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['registrar.Student']"})
        }
    }

    complete_apps = ['registrar']
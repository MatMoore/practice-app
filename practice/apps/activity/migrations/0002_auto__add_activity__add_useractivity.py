# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Activity'
        db.create_table('activity_activity', (
            ('activity_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('activity', ['Activity'])

        # Adding model 'UserActivity'
        db.create_table('activity_useractivity', (
            ('user_activity_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('activity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['activity.Activity'])),
            ('streak_first_checkin', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_checkin', self.gf('django.db.models.fields.DateTimeField')()),
            ('swag', self.gf('django.db.models.fields.IntegerField')(default=100)),
        ))
        db.send_create_signal('activity', ['UserActivity'])


    def backwards(self, orm):
        # Deleting model 'Activity'
        db.delete_table('activity_activity')

        # Deleting model 'UserActivity'
        db.delete_table('activity_useractivity')


    models = {
        'activity.activity': {
            'Meta': {'object_name': 'Activity'},
            'activity_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'activity.useractivity': {
            'Meta': {'object_name': 'UserActivity'},
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['activity.Activity']"}),
            'last_checkin': ('django.db.models.fields.DateTimeField', [], {}),
            'streak_first_checkin': ('django.db.models.fields.DateTimeField', [], {}),
            'swag': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'user_activity_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['activity']
# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'UserActivity.last_checkin'
        db.alter_column('activity_useractivity', 'last_checkin', self.gf('django.db.models.fields.DateTimeField')(null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'UserActivity.last_checkin'
        raise RuntimeError("Cannot reverse this migration. 'UserActivity.last_checkin' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'UserActivity.last_checkin'
        db.alter_column('activity_useractivity', 'last_checkin', self.gf('django.db.models.fields.DateTimeField')())

    models = {
        'activity.activity': {
            'Meta': {'object_name': 'Activity'},
            'activity_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'activity.useractivity': {
            'Meta': {'object_name': 'UserActivity'},
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['activity.Activity']"}),
            'last_checkin': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'streak_first_checkin': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'swag': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'user_activity_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['activity']
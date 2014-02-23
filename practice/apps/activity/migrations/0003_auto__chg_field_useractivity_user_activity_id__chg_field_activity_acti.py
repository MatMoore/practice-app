# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Changing field 'UserActivity.user_activity_id'
        #db.alter_column('activity_useractivity', 'user_activity_id', self.gf('django.db.models.fields.AutoField')(primary_key=True))

        #http://south.aeracode.org/ticket/407
        db.execute("CREATE SEQUENCE activity_useractivity_user_activity_id_seq")
        db.execute("SELECT setval('activity_useractivity_user_activity_id_seq', (SELECT MAX(user_activity_id) FROM activity_useractivity))")
        db.execute("ALTER TABLE activity_useractivity ALTER COLUMN user_activity_id SET DEFAULT nextval('activity_useractivity_user_activity_id_seq'::regclass)")
        db.execute("ALTER SEQUENCE activity_useractivity_user_activity_id_seq OWNED BY activity_useractivity.user_activity_id")

        # Changing field 'activity_activity.activity_id'
        #db.alter_column('activity_activity', 'activity_id', self.gf('django.db.models.fields.AutoField')(primary_key=True))
        db.execute("CREATE SEQUENCE activity_activity_activity_id_seq")
        db.execute("SELECT setval('activity_activity_activity_id_seq', (SELECT MAX(activity_id) FROM activity_activity))")
        db.execute("ALTER TABLE activity_activity ALTER COLUMN activity_id SET DEFAULT nextval('activity_activity_activity_id_seq'::regclass)")
        db.execute("ALTER SEQUENCE activity_activity_activity_id_seq OWNED BY activity_activity.activity_id")

    def backwards(self, orm):

        # Changing field 'activity_useractivity.user_activity_id'
        #db.alter_column('activity_useractivity', 'user_activity_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True))
        db.execute("ALTER TABLE activity_useractivity ALTER COLUMN user_activity_id DROP DEFAULT")
        db.execute("DROP SEQUENCE activity_useractivity_user_activity_id_seq")

        # Changing field 'activity_activity.activity_id'
        #db.alter_column('activity_activity', 'activity_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True))
        db.execute("ALTER TABLE activity_activity ALTER COLUMN activity_id DROP DEFAULT")
        db.execute("DROP SEQUENCE activity_activity_activity_id_seq")

    models = {
        'activity.activity': {
            'Meta': {'object_name': 'Activity'},
            'activity_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'activity.useractivity': {
            'Meta': {'object_name': 'UserActivity'},
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['activity.Activity']"}),
            'last_checkin': ('django.db.models.fields.DateTimeField', [], {}),
            'streak_first_checkin': ('django.db.models.fields.DateTimeField', [], {}),
            'swag': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'user_activity_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['activity']

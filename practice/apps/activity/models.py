"""
Activity models
"""
from django.db import models
import datetime
import pytz

class Activity(models.Model):
    '''
    Something that can be practiced
    '''
    activity_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

class UserActivity(models.Model):
    '''
    An activity the user is practicing
    '''
    user_activity_id = models.AutoField(primary_key=True)
    activity = models.ForeignKey('Activity')
    streak_first_checkin = models.DateTimeField(null=True)
    last_checkin = models.DateTimeField(null=True)
    swag = models.IntegerField(default=100)

    def is_streak(self):
        """Has this been practiced in the last day?
        We consider the current day to start from 5AM local time.
        Note that this can be more than 24 hours ago!"""
        # TODO use local timezone
        if not self.last_checkin:
            return False
        checkin_date = (self.last_checkin - datetime.timedelta(hours=5)).date()
        today = datetime.date.today()
        return (today - checkin_date).days <= 1

    def current_streak(self):
        '''Length of current streak in days.'''
        if not self.is_streak():
            return 0
        return (self.last_checkin - self.streak_first_checkin).days + 1

    def checkin(self, swag=100):
        '''Register a practice session.'''
        now = datetime.datetime.now(pytz.utc)
        if not self.is_streak():
            self.streak_first_checkin = now
        self.last_checkin = now
        self.swag += swag

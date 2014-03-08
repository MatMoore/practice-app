from django.test import TestCase
from .models import UserActivity as UA
from freezegun import freeze_time

@freeze_time('2000-01-01 12:00:00')
class StreakTest(TestCase):
    fixtures = ['user_activities.json']

    def setUp(self):
        self.never_practiced = UA.objects.get(activity__name='never_practiced')
        self.practiced_today = UA.objects.get(activity__name='first_practiced_2000')
        self.extended_today = UA.objects.get(activity__name='streak_extended_2000')
        self.not_extended_today = UA.objects.get(activity__name='streak_not_extended_2000')
        self.no_streak = UA.objects.get(activity__name='streak_broken_2000')
        super(StreakTest, self).setUp()

    # Initial conditions
    def test_never_practiced(self):
        self.assertFalse(self.never_practiced.is_streak())
        self.assertEqual(self.never_practiced.current_streak(), 0)

    def test_practiced_today(self):
        self.assertTrue(self.practiced_today.is_streak())
        self.assertEqual(self.practiced_today.current_streak(), 1)

    def test_extended_today(self):
        self.assertTrue(self.extended_today.is_streak())
        self.assertEqual(self.extended_today.current_streak(), 366)

    def test_not_extended_today(self):
        self.assertTrue(self.not_extended_today.is_streak())
        self.assertEqual(self.not_extended_today.current_streak(), 365)

    def test_no_streak(self):
        self.assertFalse(self.no_streak.is_streak())
        self.assertEqual(self.no_streak.current_streak(), 0)

    # Checkin
    def test_checkin_extends(self):
        activities = [self.never_practiced, self.not_extended_today, self.no_streak]
        for activity in activities:
            previous_streak = activity.current_streak()
            activity.checkin()
            self.assertEqual(activity.current_streak(), previous_streak + 1)
            self.assertTrue(activity.is_streak())

    def test_checkin_doesnt_extend(self):
        activities = [self.practiced_today, self.extended_today]

        for activity in activities:
            previous_streak = activity.current_streak()
            activity.checkin()
            self.assertEqual(activity.current_streak(), previous_streak)
            self.assertTrue(activity.is_streak())

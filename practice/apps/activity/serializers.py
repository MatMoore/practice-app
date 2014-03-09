from .models import UserActivity, Activity
from rest_framework import serializers

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('activity_id', 'name')

class UserActivitySerializer(serializers.ModelSerializer):
    current_streak = serializers.Field(source='current_streak')
    streak_continued_today = serializers.Field(source='streak_continued_today')
    activity = ActivitySerializer()

    class Meta:
        model = UserActivity
        fields = ('activity', 'swag', 'last_checkin', 'current_streak',
                'streak_continued_today')


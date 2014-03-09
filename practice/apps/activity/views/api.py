from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from ..models import UserActivity, Activity
from ..serializers import UserActivitySerializer, ActivitySerializer
from rest_framework_nested.routers import SimpleRouter, NestedSimpleRouter
from rest_framework.response import Response
from django.conf.urls import patterns, include, url

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class UserActivityViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_field = 'activity_id'
    queryset = UserActivity.objects.all()
    serializer_class = UserActivitySerializer

class CheckinViewSet(viewsets.ViewSet):
    def create(self, request, activity_activity_id):
        ua, created = UserActivity.objects.get_or_create(activity_id=activity_activity_id)
        ua.checkin()
        serializer = UserActivitySerializer(ua)
        return Response(serializer.data)

router = SimpleRouter()
router.register(r'activities', ActivityViewSet)
router.register(r'users/123/activities', UserActivityViewSet)

activity_router = NestedSimpleRouter(router, r'users/123/activities', lookup='activity')
activity_router.register(r'checkins', CheckinViewSet, 'checkin')

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^', include(activity_router.urls)),
)

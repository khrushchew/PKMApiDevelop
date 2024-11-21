from django.urls import path, include
from rest_framework import routers

from .views.BIG_CALENDAR_view import BIG_CALENDAR_Api_View

BIG_CALENDAR_router = routers.SimpleRouter()
BIG_CALENDAR_router.register(r'big_calendars', BIG_CALENDAR_Api_View, 'big_calendar')


urlpatterns = [
    path('', include(BIG_CALENDAR_router.urls))
]

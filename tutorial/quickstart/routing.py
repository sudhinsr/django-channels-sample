from django.urls import re_path
from tutorial.quickstart.consumer import NotificationConsumer

websocket_urlpatterns = [
    re_path(r'ws/notification/(?P<room_name>\w+)/$', NotificationConsumer),
]
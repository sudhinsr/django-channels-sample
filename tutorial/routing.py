from django.urls import re_path
from channels.routing import ProtocolTypeRouter, URLRouter
from tutorial.quickstart.consumer import NotificationConsumer
from django.urls import path

websockets = URLRouter([
    path(
        'ws/notification/', NotificationConsumer
        # "ws/", NotificationConsumer, name="notification",
    ),
])

application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    "websocket": websockets
})
from rest_framework.views import Response,APIView
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import json

class TestViewSet(APIView):

    def get(self, content):
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)("notify_django", {
                'type': 'send_message',
                'message': "group from view"
        })
        
        return Response({"status": True})

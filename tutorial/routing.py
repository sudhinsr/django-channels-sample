from channels.routing import ProtocolTypeRouter, URLRouter
import tutorial.quickstart.routing
from channels.auth import AuthMiddlewareStack


application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
             tutorial.quickstart.routing.websocket_urlpatterns
        )
    ),
})

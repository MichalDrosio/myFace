import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
import Message.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Face.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            Message.routing.websocket_urlpatterns
        )
    )
})
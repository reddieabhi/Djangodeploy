# routing.py

from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from . import consumers

application = ProtocolTypeRouter({
    "websocket": URLRouter(
        [
            path("ws/time/", consumers.TimeConsumer.as_asgi()),
        ]
    ),
    # Add this to handle non-websocket protocols
    "http": get_asgi_application(),
})

"""
ASGI config for RealTime project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from myapp.consumer import *

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RealTime.settings')

application = get_asgi_application()

ws_pattern = [
   path("ws/main/", MainConsumer)
]

application = ProtocolTypeRouter({
   "websocket": (
        (
            URLRouter(ws_pattern)
        )
    ),
})

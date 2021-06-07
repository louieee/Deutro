import os

from channels.routing import ProtocolTypeRouter, get_default_application
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Deutro.settings')

application = get_default_application()
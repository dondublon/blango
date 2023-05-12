"""
ASGI config for blango project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blango.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Dev')

# from django.core.asgi import get_asgi_application
from configurations.asgi import get_asgi_application


application = get_asgi_application()

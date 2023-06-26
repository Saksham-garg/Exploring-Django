"""
ASGI config for QuizApp_Django_Plus_Vuejs project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'QuizApp_Django_Plus_Vuejs.settings')

application = get_asgi_application()

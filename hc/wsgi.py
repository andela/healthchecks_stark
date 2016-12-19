"""
WSGI config for hc project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise
<<<<<<< HEAD

=======
>>>>>>> 1e842f9e049b8a5b4cf160f368a816ab9c2d42e8

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hc.settings")



application = get_wsgi_application()
<<<<<<< HEAD
application = DjangoWhiteNoise(application)
=======
application = DjangoWhiteNoise(application)
>>>>>>> 1e842f9e049b8a5b4cf160f368a816ab9c2d42e8

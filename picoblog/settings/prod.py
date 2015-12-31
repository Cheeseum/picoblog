from .common import *

MIDDLEWARE_CLASSES += (
    'django.middleware.security.SecurityMiddleware',
)

X_FRAME_OPTIONS = 'DENY'

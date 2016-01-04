from .common import *

MIDDLEWARE_CLASSES += (
    'django.middleware.security.SecurityMiddleware',
)

X_FRAME_OPTIONS = 'DENY'
    
ALLOWED_HOSTS = []

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/var/log/picoblog/debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        }
    }
}

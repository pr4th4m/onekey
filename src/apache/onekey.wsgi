import os, sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.getcwd(), os.path.pardir))
sys.path.append(PROJECT_ROOT+'/onekey')
sys.path.append(PROJECT_ROOT)

os.environ['DJANGO_SETTINGS_MODULE'] = 'onekey.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

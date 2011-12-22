import os, sys

sys.path.append('/home/pratz/webapps/onekey/src/onekey')
sys.path.append('/home/pratz/webapps/onekey/src')

os.environ['DJANGO_SETTINGS_MODULE'] = 'onekey.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

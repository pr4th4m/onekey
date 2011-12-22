
import subprocess
import ipdb

ipdb.set_trace()

p = subprocess.Popen(["/var/www/onekey/manage.py","show_urls"],stdout=subprocess.PIPE)

data, errors = p.communicate()

print data

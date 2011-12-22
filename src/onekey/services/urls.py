from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('services.views',
                      (r'^display/$', 'display'),

)

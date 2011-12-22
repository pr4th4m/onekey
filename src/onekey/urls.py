from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # admin site urls
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),


    url(r'^$', 'views.index', name="index" ),
    url(r'^services/', include('services.urls')),
    url(r'^usr/', include('usr.urls')),

    # url(r'^(?P<organization>[a-z]+)/$', 'views.org',
    #     { 'template_name':'index.html', 'model_name':'test_model'}, name = "organize"),
)

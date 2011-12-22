from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'onekey.views.home', name='home'),
    # url(r'^onekey/', include('onekey.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

    url(r'^$', 'views.index', name="index" ),
    url(r'^(?P<organization>[a-z]+)/$', 'views.org',
        { 'template_name':'index.html', 'model_name':'test_model'}, name = "organize"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^services/', include('services.urls')),
    url(r'^usr/', include('usr.urls')),
)

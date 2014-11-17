from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.site.site_header = 'ASD'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'asd.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include(admin.site.urls)),
)

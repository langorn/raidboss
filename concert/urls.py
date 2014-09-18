from django.conf.urls import patterns, include, url
from crm import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'concert.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^crm/',include('crm.urls')),
    url(r'^teammate/',include('teammate.urls'))
)

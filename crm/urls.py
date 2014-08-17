from django.conf.urls import patterns, url
from crm import views


urlpatterns = patterns('',
	url(r'^$',views.index, name='index'),
	url(r'^grab_data/',views.grab_data,name="grab_data")
)
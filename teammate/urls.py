from django.conf.urls import patterns, url
from teammate import views

urlpatterns = patterns('',
	url(r'^$',views.index, name='index'),
	

	#user related
	url(r'^profile/$',views.profile, name='profile'),
	url(r'^register/$',views.register, name='register'),
	url(r'^login/$',views.user_login, name='user_login'),
	url(r'^chat/$',views.chat, name='chat'),
	url(r'^call/(?P<peer_id>.+)/$',views.call_to, name='call_to'),
	url(r'^findUserByDB/$',views.findUserByDB, name='findUserByDB'),
	url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/login?next=123'}),


	#post related
	url(r'^quest/post/$',views.post_quest, name='post_quest'),
	url(r'^getInstance/(?P<game_id>\d+)/$',views.getInstance, name='getInstance'),
	url(r'^getAttrs/(?P<game_id>\d+)/$',views.getAttrs, name='getAttrs'),
	url(r'^post_verify/$',views.post_verify,name='post_verify'),
	
	#ajax
	url(r'^ajax_search/(?P<keyword>.+)/$',views.ajax_search,name='ajax_search'),
	
	#search for topic
	url(r'^topic/search/(?P<game_id>.+)/(?P<instance_name>.+)/$',views.topic_search,name='topic_search'),
	url(r'^topics/$',views.topics, name='topics'),
	url(r'^topic/(?P<topic_id>\d+)/$',views.get_topic, name='topic_get'),
	
	#create comment
	url(r'^comment/create/(?P<topic_id>\d+)/$',views.post_comment,name='comment_create'),
	

)
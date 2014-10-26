from django.conf.urls import patterns, url
from teammate import views

urlpatterns = patterns('',
	url(r'^$',views.index, name='index'),
	

	#user related
	url(r'^profile/$',views.profile, name='profile'),
	url(r'^register/$',views.register, name='register'),
	url(r'^login/$',views.user_login, name='user_login'),
	url(r'^chat/$',views.chat, name='chat'),
	url(r'^call/(?P<chatroom>.+)/$',views.call_to, name='call_to'),
	url(r'^findUserByDB/$',views.findUserByDB, name='findUserByDB'),
	url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/login?next=123'}),
	url(r'^character/save/',views.save_character,name='save_character'),
	url(r'^user_desc/save/',views.save_userdesc,name='save_userdesc'),
	url(r'^user_attitude/save/',views.save_attitude,name='save_attitude'),

	#webrtc
	url(r'^save_peer_code/$',views.save_peer_code,name='save_peer_code'),


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
	
	#search for job & race
	url(r'^race/(?P<game_id>\d+)/$',views.race_search, name='race_search'),
	url(r'^job/(?P<game_id>\d+)/$',views.job_search, name='job_search'),


	#create comment
	url(r'^comment/create/(?P<topic_id>\d+)/$',views.post_comment,name='comment_create'),
	

)
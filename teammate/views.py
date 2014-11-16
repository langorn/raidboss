from django.shortcuts import render, render_to_response
from teammate.forms import UserForm, UserProfileForm, TopicForm
from teammate.models import Game, Instance, Attributes,Comment
from django.db.models import Q

from django import forms
from django.http import HttpResponse, HttpResponseForbidden
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
import json

import os
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.forms.models import inlineformset_factory
from teammate.forms import RequirementForm, AttitudeForm, RequireForm
from teammate.models import Requirement, Topic, Chatroom, Personality, UserType, Race, Job, Character, UserProfile
from django.core.context_processors import csrf

# Create your views here.
def index(request):

	game = Game.objects.all()
	return render(request,'teammate/index.html',{'game':game})


# user login by FB
def findUserByDB(request):
    facebook_id = request.GET.get('facebook_id')
    name = request.GET.get('name')
    email = request.GET.get('email')
    gender = request.GET.get('gender')
    if facebook_id:
        try:
			user = User.objects.get(email=email) #UserProfile.objects.get(facebook_id=facebook_id)
			user.backend = 'django.contrib.auth.backends.ModelBackend'
			login(request, user)
        except:
            registered = False
            password = User.objects.make_random_password()
            user = User.objects.create_user(email, email, password)
            profile = UserProfile(user=user,description='facebook',facebook_id=facebook_id,gender=gender)
            profile.save()
            registered = True

            #db.session.add(user)
            #db.session.commit()
            #session['user'] = user
        	#request.session['user'] = user ;

    return HttpResponseRedirect('/')


def user_login(request):
	context = RequestContext(request)
	if request.method == 'POST':
		user = request.POST['username']	
		password = request.POST['password']
		next = request.POST['next']
		user = authenticate(username=user, password=password)
		if user is not None:
			if user.is_active:
				print 'useris active'
				login(request, user)
				return HttpResponseRedirect('/')
			else:
				return HttpResponseRedirect('/') #("Invalid login details supplied")
		else:
			return HttpResponseRedirect('/register')
	else:
		next = request.GET['next']
		return render_to_response('user_login.html',{'next':next},context)


@login_required(login_url='/login/?next=/')
def profile(request):
	user = request.user
	userprofile = UserProfile.objects.filter(user=user)
	description = ''
	for u in userprofile:
		print u
		description = u.description
		attitude = u.attitude


	own_att = []
	try:
		atts = attitude.split(',')
		for att in atts:
			try:
				user_type = UserType.objects.get(pk=att)
				own_att.append(user_type)
			except:
				pass
	except:
		pass

	personality = UserType.objects.all()
	game = Game.objects.all()
	character = Character.objects.filter(user=user)

	return render(request,'profile.html',{'personality':personality,'game':game,'character':character,'description':description,'own_att':own_att})

def logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def register(request):
	context = RequestContext(request)
	registered = False
	if request.method == 'POST':
		
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()

			user.set_password(user.password)
			user.save()
			profile = profile_form.save(commit=False)
			profile.user = user
			profile.save()
			registered = True
			return HttpResponseRedirect('/')
		else:
			print user_form.errors, profile_form.errors
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()
	return render_to_response('register.html',
		{'user_form':user_form, 'profile_form':profile_form, 'registered':registered},
		context)

def post_quest(request):
	game = Game.objects.all()
	context = RequestContext(request)
	if request.method == 'POST':
		topic_form = TopicForm(data=request.POST)
		formset = request.GET.get('formset')

		if topic_form.is_valid():
			topic = topic_form.save(commit=False)
			topic.owner_name = request.user
			topic.save()
		
		if formset.is_valid():
			formset.save()

			game_id = request.POST['game']
			print game_id
			theGame = Game.objects.get(pk=game_id)
			game_count = Topic.objects.filter(game=theGame).count()
			theGame.post_count = game_count
			theGame.save()
			print theGame


			return HttpResponseRedirect('/')

		else:
			#print formset
			return HttpResponseRedirect('/quest/post/')
	else:
		topic_form = TopicForm()
		items_formset = inlineformset_factory(Topic,Requirement,form=RequirementForm,extra=1)
		items_forms = items_formset()
		require_form = RequireForm()
		#print items_forms
		return render_to_response('post_quest.html',{'topic_form':topic_form, 'items_forms':items_forms, 'game':game, 'require_form':require_form},context)


def post_verify(request):

	user = request.user
	if not user:
		return HttpResponseRedirect('/login/?next=/')

	if request.method == 'POST':
		instanceNo = request.POST.get('Instance')
		instances = Instance.objects.get(pk=instanceNo)
		topic_form = TopicForm(data=request.POST)
		RequirementInlineFormset = inlineformset_factory(Topic,Requirement)

		if topic_form.is_valid():
			topic = topic_form.save(commit=False)
			topic.owner_name = request.user
			topic.Instance = instances
			topic.save()

		require_form =RequireForm(request.POST)
		if require_form.is_valid():
			requirements = require_form.save(commit=False)
			requirements.topics = topic
			requirements.games = topic.game_name
			requirements.save() 

		game_id = request.POST.get('game_name')
		theGame = Game.objects.get(pk=game_id)
		game_count = Topic.objects.filter(game_name=theGame).count()
		theGame.post_count = game_count
		theGame.save()

		instance_count = Topic.objects.filter(Instance=instances).count() #Instance.objects.filter(pk=instanceNo).count()
		instances.post_count = instance_count
		instances.save()

	return HttpResponseRedirect('/')
		# formset = RequirementInlineFormset(request.POST)
		# print formset
		# if formset.is_valid():
		# 	requirements = formset.save(commit=False)
		# 	print requirements
		# 	for requirement in requirements:
		# 		requirement.topics = topic
		# 		requirement.save()

		# 	return HttpResponseRedirect('/')

		# else:
		# 	return HttpResponseRedirect('/quest/post')

#dynamic form value change
def getInstance(request,game_id):
	result_list = Instance.objects.filter(Q(game__exact=game_id))
	context = {'result_list':result_list}
	data = serializers.serialize('json',result_list)
	return HttpResponse(data, mimetype="application/json")

def getAttrs(request,game_id):
	result_list = Attributes.objects.filter(Q(game__exact=game_id))
	context = {'result_list':result_list}
	data = serializers.serialize('json',result_list)
	return HttpResponse(data, mimetype="application/json")

def form_valid(request):
	formset = request.GET.get('formset')
	if formset.is_valid():
		formset.save()
	return None

def ajax_search(request,keyword):
	result_list = Instance.objects.filter(Q(name__contains=keyword))
	context = {'result_list':result_list}
	data = serializers.serialize('json', result_list, fields=('name'))
	return HttpResponse(data, mimetype="application/json") 

@login_required(login_url='/login/?next=/')
def race_search(request, game_id):
	result_list = Race.objects.filter(Q(game_id__exact=game_id ))
	result = serializers.serialize('json', result_list)
	return HttpResponse(result,mimetype="application/json")

@login_required(login_url='/login/?next=/')
def job_search(request, game_id):
	result_list = Job.objects.filter(Q(game_id__exact=game_id ))
	result = serializers.serialize('json', result_list)
	return HttpResponse(result,mimetype="application/json")


def topic_search(request, game_id, instance_name):
	result_list = Topic.objects.filter(Q(game_name__exact=game_id )& Q(Instance__name__contains=instance_name))
	result = serializers.serialize('json', result_list)
	return HttpResponse(result,mimetype="application/json")

def topic_by_instance(request, game_id, instance_id):
	result_list = Topic.objects.filter(Q(game_name__exact=game_id )& Q(Instance__pk__exact=instance_id))
	result = serializers.serialize('json', result_list)
	return HttpResponse(result,mimetype="application/json")



def topics(request):
	result_list = Topic.objects.all()
	result = serializers.serialize('json', result_list)
	return HttpResponse(result,mimetype="application/json")

def get_topic(request,topic_id):
	topic = Topic.objects.get(pk=topic_id)

	requirement = Requirement.objects.filter(topics=topic)
	try:
		comments = Comment.objects.filter(topic_name=topic)
	except:
		comments = []
	print topic

	# try:
	# 	requirement = Requirement.objects.get(pk=topic_id)
	# except:
	# 	requirement = []
	context = {'topic':topic,'comments':comments, 'requirement':requirement}	
	return render(request,'topic.html',context)

@login_required(login_url='/login/?next=/')
def post_comment(request,topic_id):
	topic = Topic.objects.get(pk=topic_id)
	user = request.user
	msg = request.POST.get('message')
	cm = Comment(topic_name=topic, user_name=user,message=msg)
	cm.save()
	return HttpResponseRedirect('/')
def chat(request):
	return render(request,'chat.html')

def call_to(request,chatroom):
	ct_room = Chatroom.objects.get(name=chatroom)
	print ct_room
	if ct_room:
		context = {'peer_id':ct_room.peer_code}
	return render(request, 'call.html',context)

@login_required(login_url='/login/?next=/')
def save_peer_code(request):
	peer_code = request.POST['id']
	print peer_code
	user = request.user 
	try:
		result = Chatroom.objects.get(user=request.user)
		result.peer_code = peer_code
		result.save()
	except:
		ct = Chatroom(user=user,peer_code=peer_code,name=user.username)
		ct.save()

	return HttpResponse('/')

@login_required(login_url='/login/?next=/')
def save_character(request):
	user = request.user
	game_id = request.POST['game_id']
	race_id = request.POST['race_id']
	job_id = request.POST['job_id']
	name = request.POST['name']
	desc = request.POST['desc']

	game = Game.objects.get(pk=game_id)
	race = Race.objects.get(pk=race_id)
	job = Job.objects.get(pk=job_id)

	character = Character(name=name, user=user, game=game, race=race, job=job, desc=desc)
	character.save()

	return HttpResponse('/profile')

@login_required(login_url='/login/?next=/')
def save_userdesc(request):
	user = request.user
	try:
		userprofile = UserProfile.objects.get(user=user)
		userprofile.description = request.POST['desc']
		userprofile.save()
		#print 1
	except:
		profile_form = UserProfileForm(data=request.POST)
		user_profile = profile_form.save(commit=False)
		user_profile.user = user
		user_profile.save()
		#print 2


	return HttpResponse('/profile')

@login_required(login_url='/login/?next=/')
def save_attitude(request):
	user = request.user
	try:
		#print 1
		userprofile = UserProfile.objects.get(user=user)
		userprofile.attitude = request.POST['attitude']
		userprofile.save()
	except:
		#print 2
		profile_form = AttitudeForm(data=request.POST)
		user_profile = profile_form.save(commit=False)
		user_profile.user = user
		user_profile.save()

	return HttpResponse('/profile')


def list_game(request):
	result_list = Game.objects.all()
	result = serializers.serialize('json', result_list)
	return HttpResponse(result, mimetype="application/json")

def list_dungeon(request, game_id):
	result_list = Instance.objects.filter(Q(game_id__exact=game_id))
	result = serializers.serialize('json', result_list)
	return HttpResponse(result, mimetype="application/json")
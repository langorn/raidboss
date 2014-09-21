from django.shortcuts import render, render_to_response
from teammate.forms import UserForm, UserProfileForm, TopicForm
from teammate.models import Game, Instance, Attributes
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
from teammate.forms import RequirementForm
from teammate.models import Requirement, Topic
from django.core.context_processors import csrf

# Create your views here.
def index(request):

	game = Game.objects.all()
	return render(request,'teammate/index.html',{'game':game})

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
				return HttpResponseRedirect(next)
			else:
				return HttpResponse("Invalid login details supplied")
	else:
		next = request.GET['next']
		return render_to_response('user_login.html',{'next':next},context)



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

	context = RequestContext(request)
	if request.method == 'POST':
		topic_form = TopicForm(data=request.POST)
		formset = request.GET.get('formset')

		if topic_form.is_valid():
			topic = topic_form.save(commit=False)
			print request.user
			topic.owner_name = request.user
			topic.save()
		
		if formset.is_valid():
			formset.save()

			return HttpResponseRedirect('/')

		else:
			return HttpResponseRedirect('/teammate/post_quest')
	else:
		topic_form = TopicForm()
		items_formset = inlineformset_factory(Topic,Requirement,form=RequirementForm,extra=1)
		items_forms = items_formset()
		print items_forms
		return render_to_response('post_quest.html',{'topic_form':topic_form, 'items_forms':items_forms},context)

def post_verify(request):
	if request.method == 'POST':
		instanceNo = request.POST.get('instance')
		instances = Instance.objects.get(pk=instanceNo)
		topic_form = TopicForm(data=request.POST)
		print topic_form
		RequirementInlineFormset = inlineformset_factory(Topic,Requirement)

		if topic_form.is_valid():
			topic = topic_form.save(commit=False)
			topic.owner_name = request.user
			topic.Instance = instances
			topic.save()

		formset = RequirementInlineFormset(request.POST)
		if formset.is_valid():
			requirements = formset.save(commit=False)

			for requirement in requirements:
				requirement.topics = topic
				requirement.save()

			return HttpResponseRedirect('/')

		else:
			return HttpResponseRedirect('/teammate/post_quest')

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

def topic_search(request, game_id, instance_name):
	result_list = Game.objects.filter(Q(pk__exact=game_id )& Q(instance__name__contains=instance_name))
	result = serializers.serialize('json', result_list)
	return HttpResponse(result,mimetype="application/json")

def topics(request):
	result_list = Topic.objects.all()
	result = serializers.serialize('json', result_list)
	return HttpResponse(result,mimetype="application/json")

def get_topic(request,topic_id):
	topic = Topic.objects.get(pk=topic_id)
	print topic
	context = {'topic':topic}	
	return render(request,'topic.html',context)

def chat(request):
	return render(request,'chat.html')

def call_to(request,peer_id):
	context = {'peer_id':peer_id}
	return render(request, 'call.html',context)

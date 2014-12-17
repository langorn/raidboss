# from crm.models import UserProfile
from django.contrib.auth.models import User
from django import forms
from teammate.models import Topic, Requirement, UserProfile
from django.forms.models import inlineformset_factory
from django.views.generic import CreateView
from django.shortcuts import redirect

#from teammate import RequirementForm, RequirementFormSet


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('email','username','password')


class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('description',)

class AttitudeForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('attitude',)


class TopicForm(forms.ModelForm):
	class Meta:
		model = Topic
		labels = {
            'remark': ('Description'), 'game_name':('Game')
        }
		exclude = ('Instance','owner_name','status','state','chatroom','quantity')


class RequireForm(forms.ModelForm):
	class Meta:
		model = Requirement
		exclude = ('games','topics')


	# games = models.ForeignKey(Game ,related_name="topic_games")
	# tank = models.IntegerField(max_length=200)
	# healer = models.IntegerField(max_length=200)
	# dpser = models.IntegerField(max_length=200)
	# teammate = models.IntegerField(max_length=200)
	# topics = models.ForeignKey(Topic,related_name="topic_requirement")

class RequirementForm(forms.ModelForm):
	class Meta:
		model = Requirement

RequirementFormSet = inlineformset_factory(Topic,Requirement)


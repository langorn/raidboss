from crm.models import UserProfile
from django.contrib.auth.models import User
from django import forms
from teammate.models import Topic, Requirement
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


class TopicForm(forms.ModelForm):
	class Meta:
		model = Topic
		exclude = ('owner_name','Instance','status','state','chatroom')


class RequirementForm(forms.ModelForm):
	class Meta:
		model = Requirement

RequirementFormSet = inlineformset_factory(Topic,Requirement)


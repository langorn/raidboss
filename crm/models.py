from django.db import models
from django.contrib.auth.models import User
import scrapy
from scrapy.contrib.djangoitem import DjangoItem

class Topic(models.Model):
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	owner = models.ForeignKey(User)
	created_date = models.DateTimeField(auto_now=True)
	status = models.BooleanField()

class GrabData(models.Model):
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	owner = models.ForeignKey(User)
	created_date = models.DateTimeField(auto_now=True)
	status = models.BooleanField()

class TopicItem(DjangoItem):
	django_model = GrabData

class MainRole(models.Model):
	name = models.CharField(max_length=200)
	role = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	created_date = models.DateTimeField(auto_now=True)
	facebook = models.CharField(max_length=200)
	twitter = models.CharField(max_length=200)
	remark = models.CharField(max_length=200)
	status = models.BooleanField()

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	description = models.CharField(max_length=128, null= True,blank=True)
	facebook_id = models.CharField(max_length=128, null=True, blank=True)
	def __unicode__(self):
		return self.user.username

class SearchKeyword(models.Model):
	name = models.CharField(max_length=200)
	xpath = models.CharField(max_length=200)
	created_date = models.DateTimeField(auto_now=True)
	status = models.BooleanField()


#class Comment(models.Models):



# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
	name = models.CharField(max_length=200)
	type = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	website = models.CharField(max_length=200)

	def __unicode__(self):
		return self.name

#game related - info

class Attributes(models.Model):
	name = models.CharField(max_length=200)
	game = models.ForeignKey(Game)
	type = models.IntegerField()

	def __unicode__(self):
		return self.name

class Instance(models.Model):
	name = models.CharField(max_length=200)
	type = models.CharField(max_length=200)  #dungeon/instance/adventure
	description = models.CharField(max_length=200)
	game = models.ForeignKey(Game)

	def __unicode__(self):
		return self.name

class Skill(models.Model):
	game = models.ForeignKey(Game)
	name = models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.skill.name



# user related  - recruit post




class Topic(models.Model):
	title = models.CharField(max_length=200)
	game_name = models.ForeignKey(Game,related_name="topic_game")
	owner_name = models.ForeignKey(User,related_name="topic_targets")
	create_date = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)
	Instance = models.ForeignKey(Instance)
	#requirement = models.ForeignKey(Requirement,related_name='topic_requirement')
	quantity = models.IntegerField(max_length=200)
	state = models.CharField(max_length=200)
	status = models.BooleanField(default = True)
	remark = models.CharField(max_length=200)
	chatroom = models.CharField(max_length=200)

	def __unicode__(self):
		return self.title

class Requirement(models.Model):
	games = models.ForeignKey(Game ,related_name="topic_games")
	attributes = models.ForeignKey(Attributes)
	value = models.FloatField()
	topics = models.ForeignKey(Topic,related_name="topic_requirement")

	# def __unicode__(self):
	# 	return self.attributes


class Comment(models.Model):
	topic_name = models.ForeignKey(Topic,related_name="topic_name")
	user_name = models.ForeignKey(User,related_name="topic_users")
	message = models.CharField(max_length=200)
	created_date = models.DateTimeField(auto_now=True)
	last_modified = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return self.message

# Create your models here.

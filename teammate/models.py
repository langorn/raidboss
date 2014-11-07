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

class CharacterAttr(models.Model):
	user = models.ForeignKey(User)
	attr = models.CharField(max_length=200)
	value = models.IntegerField(max_length=200)

	def __unicode__(self):
		return self.attr

class Attributes(models.Model):
	name = models.CharField(max_length=200)
	game = models.ForeignKey(Game)
	type = models.IntegerField()

	def __unicode__(self):
		return self.name

class Race(models.Model):
	name = models.CharField(max_length=200)
	game = models.ForeignKey(Game)

	def __unicode__(self):
		return self.name

class Job(models.Model):
	name = models.CharField(max_length=200)
	game = models.ForeignKey(Game)

	def __unicode__(self):
		return self.name

class Character(models.Model):
	name = models.CharField(max_length=200)
	user = models.ForeignKey(User)
	game = models.ForeignKey(Game)
	race = models.ForeignKey(Race)
	job = models.ForeignKey(Job)
	desc = models.CharField(max_length=200)

	def __unicode__(self):
		return self.name


class Instance(models.Model):
	name = models.CharField(max_length=200)
	type = models.CharField(max_length=200)  #dungeon/instance/adventure
	description = models.CharField(max_length=200)
	game = models.ForeignKey(Game)
	priority = models.IntegerField(max_length=200,default=0)

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
	quantity = models.IntegerField(max_length=200)
	state = models.CharField(max_length=200)
	status = models.BooleanField(default = True)
	remark = models.CharField(max_length=200)
	chatroom = models.CharField(max_length=200)
	#requirement = models.ForeignKey(Requirement,related_name='topic_requirement')

	def __unicode__(self):
		return self.title

class Requirement(models.Model):
	games = models.ForeignKey(Game ,related_name="topic_games")
	tank = models.IntegerField(max_length=200)
	healer = models.IntegerField(max_length=200)
	dpser = models.IntegerField(max_length=200)
	teammate = models.IntegerField(max_length=200)
	topics = models.ForeignKey(Topic,related_name="topic_requirement")
	#attributes = models.ForeignKey(Attributes)
	#value = models.FloatField()


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


class Chatroom(models.Model):
	user = models.ForeignKey(User, related_name='user_chatroom')
	peer_code = models.CharField(max_length=128,null=True,blank = True)
	name = models.CharField(max_length=128, null = True,blank=True)
	def __unicode__(self):
		return self.user.username

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,related_name='user_profile')
    description = models.CharField(max_length=128, null= True,blank=True)
    facebook_id = models.CharField(max_length=128, null = True,blank=True)
    gender = models.CharField(max_length=128, null = True,blank=True)
    chatroom = models.ForeignKey(Chatroom, null=True,related_name="userprofile_chatroom")
    attitude = models.CharField(max_length=128, null = True, blank=True)

    def __unicode__(self):
        return self.user.username

class UserType(models.Model):
	name = models.CharField(max_length=128)
	type = models.IntegerField(max_length=128)

	def __unicode__(self):
		return self.name

class Personality(models.Model):
	user = models.ForeignKey(User,related_name='from_user')
	by_user = models.ForeignKey(User,related_name='by_user')
	like = models.ForeignKey(UserType)
	
	def __unicode__(self):
		return self.name

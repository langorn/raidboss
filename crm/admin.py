from django.contrib import admin
from crm.models import SearchKeyword, Topic, MainRole
from teammate.models import Game, Instance , Skill , Topic, Requirement, Comment , Attributes,Chatroom
from teammate.models import Personality, UserType, Race, Job, Character, UserProfile

# Register your models here.

admin.site.register(SearchKeyword)
admin.site.register(MainRole)
admin.site.register(UserProfile)


admin.site.register(Game)
admin.site.register(Instance)
admin.site.register(Skill)
admin.site.register(Topic)
admin.site.register(Requirement)
admin.site.register(Comment)
admin.site.register(Attributes)
admin.site.register(Chatroom)
admin.site.register(Personality)
admin.site.register(UserType)
admin.site.register(Race)
admin.site.register(Job)
admin.site.register(Character)

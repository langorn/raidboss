from django.contrib import admin
from crm.models import SearchKeyword, Topic, MainRole, UserProfile
from teammate.models import Game, Instance , Skill , Topic, Requirement, Comment , Attributes

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



from django.contrib import admin
from crm.models import SearchKeyword, Topic, MainRole, UserProfile
# Register your models here.

admin.site.register(SearchKeyword)
admin.site.register(Topic)
admin.site.register(MainRole)
admin.site.register(UserProfile)

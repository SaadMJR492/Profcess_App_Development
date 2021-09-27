from django.contrib import admin
from .models import RecruiterUserProfile, Job,UserData
# Register your models here.
admin.site.register(RecruiterUserProfile)
admin.site.register(Job)
admin.site.register(UserData)
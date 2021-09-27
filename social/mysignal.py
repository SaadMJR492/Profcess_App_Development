from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
#from accounts.models import ProfcessUser
from django.contrib.auth.models import User
from social.models import MyProfile

@receiver(post_save, sender=User)
def save_profile(sender,instance,created, **kwarg):
    if created:
        MyProfile.objects.create(user = instance, name= instance.username)

# from django.dispatch.dispatcher import receiver
# from django.db.models.signals import post_save
# from Profcess_Dev.settings import AUTH_USER_MODEL
# User = AUTH_USER_MODEL
# from social.models import MyProfile

# @receiver(post_save, sender=User)
# def save_profile(sender,instance,created, **kwarg):
#     if created:
#         MyProfile.objects.create(user_id = instance, name= instance.username)


# @receiver(post_save, sender=ProfcessUser)
# def create_profile(sender,instance,created, **kwarg):
#     if created:
#         MyProfile.objects.create(user_id = instance.user)

# @receiver(post_save, sender=ProfcessUser)
# def save_profile(sender,instance,**kwarg):
#     instance.myprofile.save()
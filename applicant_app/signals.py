#from django.db.models.signals import post_save
#from django.dispatch import receiver
#from .models import ApplicantUserProfile
#from .models import User
#import csv
#@receiver(post_save, sender=User)
#def create_profile(sender, instance, created, **kwargs):
 #   if created:
  #      ApplicantUserProfile.objects.create(user=instance)

#@receiver(post_save, sender=User)
#def save_profile(sender, instance, **kwargs):
 #   with open( 'my_.csv') as f:
  #      reader = csv.reader(f)
   #     for row in reader:
    #        instance.applicantuserprofile.first_name = str(row[6])
     #       instance.applicantuserprofile.last_name = str(row[7])
      #      instance.applicantuserprofile.phone = str(row[8])
       #     instance.applicantuserprofile.location = str(row[9])
        #    instance.applicantuserprofile.skill_info = str(row[10])
         #   instance.applicantuserprofile.school_degree = str(row[11])
          #  instance.applicantuserprofile.save()


from django.db import models
from django.contrib.auth.models import User
from accounts.models import ProfcessUser
#from applicant_app.models import ApplicantUserProfile
from django.db.models.deletion import CASCADE
from django.core.validators import MinValueValidator,RegexValidator
from django.contrib.auth.models import AbstractUser
#from applicant_app.models import ApplicantUserProfile
# Create your models here.
class MyProfile(models.Model):
    object = None
    #name = models.ForeignKey(ApplicantUserProfile, on_delete=models.CASCADE)
    user_id = models.OneToOneField(ProfcessUser, on_delete=models.CASCADE )
    name = models.CharField(max_length = 100)#, default=ApplicantUserProfile.first_name)
    age = models.IntegerField(default=18,validators=[MinValueValidator(18)])
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(null=True , blank=True)
    status = models.CharField(max_length= 20, default= "", choices=(("single","single"),("married","married"),("commited","commited")))
    gender = models.CharField(max_length= 20, default="", choices=(("female","female"),("male","male")))
    phone_no = models.CharField(validators=[RegexValidator("^0?[5-9]{1}\d{9}$")],max_length=15,null=True, blank=True)
    description = models.TextField(null=True,blank=True)
    #pic = models.ImageField(upload_to="images", null=True)
    def __str__(self):
        return "%s" % self.user_id

class MyPost(models.Model):
    pic = models.ImageField(upload_to="images", null=True)
    subject = models.CharField(max_length = 200)
    msg = models.TextField(null=True, blank=True)
    cr_date = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(to=MyProfile, on_delete=CASCADE, null=True, blank=True)
    def __str__(self):
        return "%s" % self.subject


# class PostComment(models.Model):
#     post_by = models.ForeignKey(to=MyPost, on_delete=CASCADE)
#     msg = models.TextField()
#     commented_by = models.ForeignKey(ProfcessUser, to_field='username', on_delete=CASCADE)
#     cr_date = models.DateTimeField(auto_now_add=True)
#     flag = models.CharField(max_length=20,null=True,blank=True,
#                               choices=(("racist", "racist"), ("abbusing", "abbusing"),))
#     def __str__(self):
#         return "%s" % self.msg

class PostComment(models.Model):
    post_by = models.ForeignKey(to=MyPost, on_delete=CASCADE)
    content = models.TextField()
    commented_by = models.ForeignKey(ProfcessUser, to_field='username', on_delete=CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    # flag = models.CharField(max_length=20,null=True,blank=True,
    #                           choices=(("racist", "racist"), ("abbusing", "abbusing"),))
    def __str__(self):
        return "%s" % self.content


class PostLike(models.Model):
    post = models.ForeignKey(to=MyPost, on_delete=CASCADE)
    liked_by = models.ForeignKey(to=MyProfile, on_delete=CASCADE)
    cr_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "%s" % self.liked_by

class FollowUser(models.Model):
    profile = models.ForeignKey(to=MyProfile, on_delete=CASCADE, related_name="profile")
    followed_by = models.ForeignKey(to=MyProfile, on_delete=CASCADE, related_name="followed_by")
    def __str__(self):
        return "%s is followed by %s" % (self.profile, self.followed_by)

#Radzzzz

class Friend_Request(models.Model):
    from_user = models.ForeignKey(
        ProfcessUser, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(
        ProfcessUser, related_name='to_user', on_delete=models.CASCADE)

    #def __str__(self):
     #   return "%s is followed by %s" % (self.profile, self.followed_by)

#Radzz code ends...

#=============================================
#bhavins task
class PostRating(models.Model):
    post = models.ForeignKey(to=MyPost, on_delete=CASCADE)
    rate = models.CharField(max_length=10,default='0')
    rate_by = models.ForeignKey(to=MyProfile, on_delete=CASCADE)
    cr_date = models.DateTimeField(auto_now_add=True)
    # def __str__(self):
    #     return str(self.pk)
    def __str__(self):
        return "%s" % self.rate_by    


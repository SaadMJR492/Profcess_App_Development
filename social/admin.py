from django.contrib import admin
from social.models import FollowUser, MyPost, MyProfile, PostComment, PostLike, Friend_Request
from django.contrib.admin.options import ModelAdmin

admin.site.register(Friend_Request)

class FollowUserAdmin(ModelAdmin):
    list_display = ["profile", "followed_by"]
    search_fields = ["profile","followed_by"]
    list_filter = ["profile","followed_by"]
admin.site.register(FollowUser,FollowUserAdmin)

class MyPostAdmin(ModelAdmin):
    list_display = ["subject", "cr_date","uploaded_by"]
    search_fields = ["subject", "msg","uploaded_by"]
    list_filter = ["cr_date", "uploaded_by"]
admin.site.register(MyPost, MyPostAdmin)

class MyProfileAdmin(ModelAdmin):
    list_display = ["name"]
    search_fields = ["name", "status","phone_no"]
    list_filter = ["status", "gender"]

admin.site.register(MyProfile, MyProfileAdmin)

# class PostCommentAdmin(ModelAdmin):
#     list_display = ["post_by", "msg"]
#     search_fields = ["msg", "post_by", "commented_by"]
#     list_filter = ["cr_date", "flag"]
# admin.site.register(PostComment, PostCommentAdmin)
admin.site.register(PostComment)

class PostLikeAdmin(ModelAdmin):
    list_display = ["post", "liked_by"]
    search_fields = ["post", "liked_by"]
    list_filter = ["cr_date"]
admin.site.register(PostLike, PostLikeAdmin)
from django.urls import path
from django.urls.conf import include
from social import views

app_name = 'social'

urlpatterns = [
    #radzz code
    path('myprofile/send_friend_request/<int:userID>/', views.send_friend_request, name='send_friend_request'),
    path('myprofile/accept_friend_request/<int:requestID>/', views.accept_friend_request,name='accept_friend_request'),
    #radzz code ends..
    path('home/', views.HomeView.as_view(), name="home"),
    path('about/', views.AboutView.as_view()),
    path('contact/', views.ContactView.as_view()),
    path('profile/edit/<int:pk>', views.MyProfileUpdateView.as_view(success_url="/social/home")),
    path('mypost/create/', views.MyPostCreate.as_view(success_url="/social/mypost")),
    path('mypost/delete/<int:pk>', views.MyPostDeleteView.as_view(success_url="/social/mypost")),
    path('mypost/', views.MyPostListView.as_view()),
    path('mypost/<int:pk>', views.MyPostDetailView.as_view()),

    path('myprofile/', views.MyProfileListView.as_view()),
    # path('myprofile/<int:pk>', views.MyProfileDetailView.as_view()),

    path('myprofile/follow/<int:pk>', views.follow),
    path('myprofile/unfollow/<int:pk>', views.unfollow),

    path('mypost/like/<int:pk>', views.like),
    path('mypost/unlike/<int:pk>', views.unlike),

    path('mypost/comment/<int:pk>', views.comment),

    path('myprofile/users/<int:pk>', views.MyProfilePostListView.as_view(), name = "myprofile-posts"),
    path('home/rate/<int:pk>', views.rate_post),

    #path('applicant/', include('applicant.urls', namespace='applicant')),
]

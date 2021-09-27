from django.urls import path, reverse_lazy,include
from . import views
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import views as auth_views

app_name = 'accounts_social'

urlpatterns =[
   # path('',views.indexViews, name="home"),
   # path('dashboard/',views.dashboardViews,name="dashboard"),
    path('', LoginView.as_view(), name='login'),
    path('register/', views.registerView, name="register_url"),
    path('index/',views.indexViews,name="index"),
    #path('accounts_social/logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('accounts_social/logout/',LogoutView.as_view(template_name='accounts_social/logout.html'),name="logout"),
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name="accounts_social/password_change_form.html",
                                                                   success_url=reverse_lazy(
                                                                       "accounts_social:password_change_done")),
         name="password_change"),
    path('change-password/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name="accounts_social/password_change_done.html"),
         name="password_change_done"),
]
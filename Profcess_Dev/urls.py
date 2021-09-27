"""Profcess_Dev URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from test_app import views
from accounts import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),

    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("findJob/", views.findJob, name="findJob"),
    path("careerAdvice/", views.careerAdvice, name="careerAdvice"),
    path("findATalent/", views.findATalent, name="findATalent"),
    path("services/", views.services, name="services"),
    path("contact/", views.contact, name="contact"),
    path("accounts/", include('accounts.urls')),
    path("recruiter/", include("recruiter_app.urls")),
    path("applicant/", include("applicant_app.urls")),
    path("college/",include("college_app.urls")),
    path("select2/", include("django_select2.urls")),
    path('', TemplateView.as_view(template_name="social_app/index.html")),  # added this
    path("accounts/", include('allauth.urls')),  # added this
    path("social/", include('social.urls', namespace='social')),
    path("accounts_social/", include('accounts_social.urls', namespace='accounts_social')),
    path('', include('chat.urls')),


path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view( template_name='accounts/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view( template_name='accounts/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
         name='password_reset_complete'),

     path('converter/',include('htmltopdf.urls'),name="converter"),
    # path("signup/", views.signup, name = "signup")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

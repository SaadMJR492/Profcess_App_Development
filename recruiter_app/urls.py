from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views
from recruiter_app.views import job_detail, Update_job,my_candidates,job_matching,search_candidates,campus_hiring,add_a_blog,assessments,recruiter_blog,applicant_detail
from django.views.static import serve
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
app_name = 'recruiter'



urlpatterns = [
    path("home/", views.home, name="home"), #<--changed this
    path("create-recruiter-user-profile/",
         views.createprofile, name="create_recruiter_profile"),
    path("<int:pk>/profile/",views.profile,name="profile"),
    path("create-job/", views.createjob, name="create_job"),
    path("posted-jobs/", views.posted_jobs, name="posted_jobs"),
    path("job-detail/<int:pk>", views.job_detail, name="job_detail"),
    path("job-detail/<int:pk>/update/", Update_job.as_view(), name = "update_job"),
    path("job-detail/<int:pk>/delete/", views.delete_job, name = "delete_job"),
    path("search-candidates/",views.search_candidates,name="search_candidates"),
# path("search-candidates/",views.search_candidates,name="search_candidates"),
   # path("search-candidates/",views.search_candidates1,name="search_candidates"),
    path("my-candidate/", views.my_candidates, name="my_candidates"),
    path("job-matching/<int:pk>", views.job_matching, name="job_matching"),
    path("campus-hiring/", views.campus_hiring, name="campus_hiring"),
    path("assessments/", views.assessments, name="assessments"),
    path("add-a-blog/", views.add_a_blog, name="add_a_blog"),
    path("recruiter-blog/", views.recruiter_blog, name="recruiter_blog"),
    path("applicant-detail/<int:pk>", views.applicant_detail, name="applicant_detail"),
    path("remove/<int:pk>",views.remove,name="remove"),
    path("view_applicants/<int:pk>",views.applicants,name="view_applicants"),
    path("can/<int:pk>",views.can,name="can"),
    path("can/<int:pk>/<int:mk>/",views.job_can,name="job_can"),
    path("alreadycan",views.alreadycan,name="alreadycan"),
    path("pricing/",views.pricing,name="pricing"),
    path("purchase-plan/",views.purchase_plan,name="purchase-plan"),
    path('<int:pk>/upload_pic/', views.upload_pic, name='upload_pic'),
    path("dashboard",views.dashboard,name='dashboard'),
    path('<int:pk>/delete_pic/', views.delete_pic, name='delete_pic'),
    path('cart_summary/',views.cart_summary,name='cart_summary'),
    path('payu_payment/',views.payu_payment,name='payment'),
     path('success/',views.success,name='success'),
    path('failure',views.failure,name='failure'),
    path('paypal_payment/',views.paypal_payment,name='paypal_payment'),
    path('plan/',views.plan,name='plan'),
    url(r'^download/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    #path('create-job/ajax/load-cities/', views.load_cities, name='ajax_load_cities'),






    # path('login/', auth_views.LoginView.as_view(),name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    # path('recruiter-signup/', views.RecruiterSignUp.as_view(), name="recruiter-signup"),
    # path('applicant-signup/', views.ApplicantSignUp.as_view(), name="applicant-signup"),
    # path('change-password/', auth_views.PasswordChangeView.as_view(template_name = "accounts/password_change_form.html", success_url = reverse_lazy("accounts:password_change_done")), name = "password_change"),
    # path('change-password/done/', auth_views.PasswordChangeDoneView.as_view(template_name = "accounts/password_change_done.html"), name = "password_change_done"),


]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

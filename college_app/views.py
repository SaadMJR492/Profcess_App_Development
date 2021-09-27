from django.shortcuts import render, get_object_or_404, redirect
from .forms import UserProfileForm,UserUpdateFormCollege,Jobs,JobUpdationForm,JobCreationForm
from .models import CollegeUserProfile, Jobs
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView, DeleteView
from django import forms
from accounts.models import ProfcessUser
from django.conf import settings
from django.core.mail import send_mail
from applicant_app.models import ApplicantUserProfile
from django.db.models import Q
from django.db.models import F
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect

# Create your views here.
# from ..recruiter_app.forms import UserUpdateForm



@login_required
def createprofile(request):
	if request.method == "POST":
		form = UserProfileForm(request.POST)
		if form.is_valid():
			userprofile = form.save(commit=False)
			userprofile.user = request.user
			userprofile.save()
			return render(request, "college_app/thanks.html")  # return page after filling userinfo form

		else:
			return "#########"

	else:
		form = UserProfileForm()
		return render(request, "college_app/userprofileform.html", {"form": form})

@login_required
def profile(request):
	if request.method == 'POST':
		c_form = UserUpdateFormCollege(request.POST, instance=request.user)

		if c_form.is_valid():
			c_form.save()
			return render(request, 'college_app/update_success.html')
	else:
		c_form = UserUpdateFormCollege(instance=request.user)
	context = {
		'c_form': c_form,

	}
	return render(request, 'college_app/profile.html', context)

@login_required
def createjob(request):
	if request.method == "POST":
		form = JobCreationForm(request.POST)
		if form.is_valid():
			job = form.save(commit=False)
			job.posted_by = request.user
			job.save()
			context = {
				"job": job,
			}
			context['job'] = job
			return render(request,"college_app/job_detail.html",context)  # return page after posting a new job
			pass
		else:
			pass
		pass
	else:
		form = JobCreationForm()
		return render(request, "college_app/createjob.html", {"form": form})
		pass



@login_required
def job_detail(request, pk=None):
    job = Jobs.objects.get(pk=pk)
    result = job.job_requirements
    mn = ApplicantUserProfile.objects.all()
    oo = ApplicantUserProfile.objects.none()
    z = []
    for mm in mn:
        jk = mm.skill_info
        for x in result:
            for y in jk:
                if x == y:
                    z.append(mm.user)
    for ui in z:
        i = ApplicantUserProfile.objects.filter(user=ui)
        oo |= i
    qs1 = job.applied_by.all()
    p = ApplicantUserProfile.objects.none()
    q = ApplicantUserProfile.objects.none()
    for k in qs1:
        qs2 = ApplicantUserProfile.objects.filter(user=k)
        p |= qs2
    q |= oo.exclude(pk__in=p)
    q |= q
    context = {
			'job': job,
			'qs': q,
			'count': len(q),
			'count1': len(p),
			'qs1': p,
		}
    context['job'] = job
    return render(request, "college_app/job_detail.html", context)

# def job_detail(request, pk=None):
# 	job = Job.objects.get(pk=pk)
# 	context={}
# 	context['job'] = job
# 	return render(request, "college_app/job_detail.html", context)

class Update_job(UpdateView):
	model=Jobs
	fields = ("primary_profile", "working_hour",
			  "notice_period", "essential_skills", "industry_type", "job_title", "job_info", 'job_vacancies',
			  "pincode", "exp_req", "cert_req", "types_of_job", "education_quali", "job_salary", "maximum",
			  "minimum", "other",
			  "city", "state", "start_date", "job_requirements", "cert", "lor", "wh", "others")
	widgets = {
		'job_title': forms.TextInput(attrs={'placeholder': 'UX/UI Designer'}),
		'city': forms.Select(attrs={'class': 'select-css'}),
		'notice_period': forms.Select(attrs={'class': 'select-css'}),
		'primary_profile': forms.Select(attrs={'class': 'select-css', }),
		'state': forms.Select(attrs={'class': 'select-css'}),
		'working_hour': forms.Select(attrs={'class': 'select-css'}),
		'industry_type': forms.Select(attrs={'class': 'select-css'}),
		'pincode': forms.TextInput(attrs={'placeholder': '123456'}),
		'job_vacancies': forms.Select(attrs={'class': 'select-css'}),
		'minimum': forms.TextInput(attrs={'placeholder': '   20,000            INR'}),
		'maximum': forms.TextInput(attrs={'placeholder': '   40,000            INR'}),
		'types_of_job': forms.Select(attrs={'class': 'select-css'}),
		'cert_req': forms.TextInput(attrs={'placeholder': 'e.g.ABC'}),
		'exp_req': forms.Select(attrs={'class': 'select-css'}),
	}
	template_name = 'college_app/createjob.html'


	def form_valid(self, form):
		form.instance.posted_by = self.request.user
		return super().form_valid(form)


def delete_job(request, pk):
	context = {}
	obj = get_object_or_404(Jobs, id=pk)
	if request.method == "POST":
		# delete object
		obj.delete()
		# after deleting redirect to
		# home page
		return HttpResponseRedirect("/college/posted-jobs/")

	return render(request, "college_app/posted_jobs.html", context)


k = ""
prof = ""

class Delete_job(DeleteView):
	model = Jobs
	success_url = '/'

@login_required
def posted_jobs(request):
	"""
	View to fetch and display the list of jobs posted by a college.
	"""

	jobs = request.user.college_jobs.all()
	context = {
		"jobs": jobs,
	}
	return render(request, "college_app/posted_jobs.html", context)


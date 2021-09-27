from django.shortcuts import render, get_object_or_404, redirect
from .forms import UserProfileForm, InputForm, UserProfileUpdationForm, PicForm, ResumeForm
from .models import ApplicantUserProfile
from recruiter_app.models import Job, RecruiterUserProfile
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_text,DjangoUnicodeDecodeError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from accounts.models import ProfcessUser
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from .token import activation_token
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.db.models import Q
from college_app.models import Jobs
# Create your views here.

@login_required
def view_profile(request, pk):
    try:
        UserProfileUpdationForm(instance=request.user.applicantuserprofile)
    except ObjectDoesNotExist:
        return redirect("applicant:create_applicant_profile")
    form = UserProfileUpdationForm(instance=request.user.applicantuserprofile)
    args = {'form': form}
    print(request.user)
    return render(request, "applicant_app/userprofileform.html", args)


@login_required
def createprofile(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST)
        p_form= UserProfileUpdationForm(request.POST,instance=request.user)
        if form.is_valid() and p_form.is_valid():
            userprofile = form.save(commit=False)
            userprofile.user = request.user
            userprofile.save()
            p_form.save()
            return render(request, "applicant_app/thanks.html") #return page after filling userinfo form

        else:
            return "#########"

    else:
        form = UserProfileForm()
        return render(request, "applicant_app/userprofileform.html", {"form":form})


@login_required
def applytojob(request, pk):
    """ Apply to a job  """
    context = {}
    job = Job.objects.get(pk=pk)
    context['job'] = job

    # If User has already applied redirect User to already applied page.
    if request.user in job.applied_by.all():
        return render(request, "applicant_app/applicationdonealready.html", context)
    job.applied_by.add(request.user)
    messages.success(request, 'Your application is received Recuiter will contact u soon')
    return render(request, "applicant_app/applytojob.html", context)
def my_jobs(request):
    job=Job.objects.all()
    l=[]
    for j in job:
        if request.user in j.applied_by.all():
            l.append(j)
    content={
        "jobs":l
    }
    return render(request, "applicant_app/my_jobs.html",content)

def withdraw_job(request,pk):

    job=Job.objects.get(pk=pk)
    job.applied_by.remove(request.user)
    job = Job.objects.all()
    l = []
    for j in job:
        if request.user in j.applied_by.all():
            l.append(j)
    content = {
        "jobs": l
    }

    return render(request, "applicant_app/my_jobs.html",content)

@login_required
def listjobs(request):
    """
    Return a list of all jobs.

    """
    jobs = Job.objects.all()
    context = {
        "jobs":jobs
    }
    #print(request.user)
    return render(request, "applicant_app/job_search.html", context)


@login_required
def job_detail(request, pk):

    job = get_object_or_404(Job, pk=pk)
    context = {
        "job":job,
    }

    return render(request, "applicant_app/job_detail.html", context)

@login_required
def mail(request):
        sub = forms.applicant_app()
        fullname = request.POST['fullname']
        mail = request.POST['mail']
        contact = request.POST['contact']
        recipient = str(sub['email'].value())
        send_mail('Verification', 'Applied successfully', 'contact@profcess.com', [recipient], fail_silently=False)
        return render(request,'applicant_app/mail.html')
def search_job(request):
    m=Job.objects.all()

    query=""
    context={}
    if request.GET:
        query=request.GET['q']
        context={
            'query':str(query)
        }
    #print(query)
    m=get_queryset(query)
    #print(m)
    flag=False
    college_jobs = Jobs.objects.all()
    for i in college_jobs:
        if i.posted_by.college_name==request.user.college_name_stu:
            print("hi")
            flag=True
            display_college_jobs=Jobs.objects.filter(posted_by=i.posted_by)
    if flag==False:
        display_college_jobs=Jobs.objects.none()



    context={
        'm':m,
        "clgjobs": display_college_jobs
    }
    return render(request, "applicant_app/job_search.html", context)
def job_searchfreshers(request):
    jobs =Job.objects.all()
    query=''
    context = {
            'query': str(query)
            }
    jobs=get_queryset(query)
    context={
		"jobs": jobs
	}
    return render(request, "applicant_app/job_search.html", context)

def job_searchwfh(request):
    jobs =Job.objects.filter(job_location="Work From Home")
    context={
        'm':jobs
    }
    return render(request, "applicant_app/job_search.html", context)

def get_queryset(query=None):
    #if (job_requirements__icontains == query):
     #   print("hi")
    #print(query)
    queryset=[]
    queries=query.split(" ")
    #print(queries)
    for ji in queries:
        jobs=Job.objects.filter(
            Q(job_title__icontains=ji) |
            Q(job_location__icontains=ji) |
            Q(job_requirements__icontains=ji)
        ).distinct()
        for j in jobs:
            queryset.append(j)
        #print(queryset)
    return list(set(queryset))

@login_required
def matching_job(request):
    applicant = request.user
    p = ApplicantUserProfile.objects.get(user=applicant)
    r=p.skill_info
    job = Job.objects.all()
    z = []
    for mm in job:
        jk = mm.job_requirements
        for x in r:
            for y in jk:
                if x == y:
                    if mm not in z:
                        z.append(mm)
    context = {
    'jobs':z
    }
    return render(request, "applicant_app/matching_job.html",context)
@login_required
def shortlist_job(request):

    return render(request,"applicant_app/shortlist_job.html")



@login_required
def job_alert(request):
    return render(request,"applicant_app/job_alert.html")

@login_required
def job_recommendations(request):
    applicant = request.user
    p = ApplicantUserProfile.objects.get(user=applicant)
    r = p.skill_info
    job = Job.objects.all()
    z = []
    for mm in job:
        jk = mm.job_requirements
        for x in r:
            for y in jk:
                if x == y:
                    if mm not in z:
                        z.append(mm)
    context = {
        'jobs': z
    }
    return render(request, "applicant_app/job_recommendations.html", context)


def job_companies(request):
    recruiter = RecruiterUserProfile.objects.all()
    return render(request,"applicant_app/job_companies.html",{'recruiter':recruiter})

@login_required
def career_guidance(request):
    return render(request,"applicant_app/career_guidance.html")

@login_required
def interview_tips(request):
    return render(request,"applicant_app/interview_tips.html")

@login_required
def expert_call(request):
    return render(request,"applicant_app/expert_call.html")


@login_required
def activate(request,uid,token):    #goes via mail
    return render(request,"applicant_app/activation.html")

@login_required
def edit_profile(request, pk):
    user = ProfcessUser.objects.get(id=pk)
    try:
        UserProfileUpdationForm(instance=request.user.applicantuserprofile)
    except ObjectDoesNotExist:
        return redirect("applicant:create_applicant_profile")
    form= UserProfileUpdationForm(instance=request.user.applicantuserprofile)
    p_form= UserProfileUpdationForm(instance=request.user)
    if request.method == "POST":
        print("hello")
        print("hello1")
        form = UserProfileUpdationForm(request.POST, instance= request.user.applicantuserprofile)
        p_form= UserProfileUpdationForm(request.POST,instance=request.user)
        if form.is_valid() and p_form.is_valid():
            form.save()
            p_form.save()
            print("-------------->name:",request.user.first_name)
            print("---------------------------------->p_name:",request.user)
            return render(request, "applicant_app/thanks.html")

    args = {'form': form,'p_form':p_form}
    return render(request, 'applicant_app/userprofileform.html', args)

@login_required
def upload_pic(request, pk):
    user = ProfcessUser.objects.get(id=pk)

    try:

        UserProfileUpdationForm(instance=request.user.applicantuserprofile)
        form= PicForm(instance=request.user.applicantuserprofile)
        if request.method == "POST":
            form = PicForm(request.POST, request.FILES, instance= request.user.applicantuserprofile)
            if form.is_valid():
                form.save()
                return render(request, "applicant_app/thanks.html")
        args = {'form': form}
        return render(request, 'applicant_app/uploadpic.html', args)
    except ObjectDoesNotExist:
        return render(request, 'applicant_app/fill_application.html')

@login_required
def upload_resume(request, pk):
        user = ProfcessUser.objects.get(id=pk)
        try:
            UserProfileUpdationForm(instance=request.user.applicantuserprofile)
            form = ResumeForm(instance=request.user.applicantuserprofile)
            if request.method == "POST":
                form = ResumeForm(request.POST, request.FILES, instance=request.user.applicantuserprofile)
                if form.is_valid():
                    form.save()
                    return render(request, "applicant_app/thanks.html")
            args = {'form': form}
            return render(request, 'applicant_app/uploadresume.html', args)
        except ObjectDoesNotExist:
            return render(request, 'applicant_app/fill_application.html')


# @login_required
# def edit_profile(request, pk):
#     #user = User.objects.get(ApplicantUserProfile, pk=pk)
#     if request.method == "POST":
#         form = UserProfileForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             #return redirect(('applicant:view_profile'))
#             return render(request, "applicant_app/thanks.html")


#     else:
#         form = UserProfileUpdationForm(instance=request.user)
#         context = {'form': form,}
#         return render(request, 'applicant_app/userprofileform.html', context)

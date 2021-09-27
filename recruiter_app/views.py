from django.shortcuts import render, get_object_or_404,redirect
from .forms import UserProfileForm, JobCreationForm, UserUpdateForm, PicForm
from .models import RecruiterUserProfile, Job
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
from paywix.payu import Payu
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger






# Create your views here.
@login_required
def home(request): #<-- Changed this
	m = ApplicantUserProfile.objects.all()
	query = ""
	location = ""
	context = {}
	if request.GET:
		query = request.GET.get('q')
		location = request.GET.get('l')

		if query is None or location is not None:
			lookups = Q(location__icontains=location)
			m = ApplicantUserProfile.objects.filter(lookups).distinct()
			context = {
				'm': m
			}
			return render(request, "recruiter_app/home.html", context)

		else:
			context = {
				'query': str(query)
			}
			m = get_queryset(query)
			can = request.user.shortlist_can.all()
			context = {
				'm': m,
				'can': can

			}
			return render(request, "recruiter_app/home.html", context)
	m = get_queryset(query)
	can = request.user.shortlist_can.all()
	context = {
		'm': m,
		'can': can

	}
	return render(request, "recruiter_app/home.html", context) #to this


@login_required
def createprofile(request):
	if request.method == "POST":
		u_form = UserProfileForm(request.POST)
		if u_form.is_valid():
			userprofile = u_form.save(commit=False)
			userprofile.user = request.user
			userprofile.save()
			return render(request, "recruiter_app/userprofileform.html", {"u_form": u_form, "successful_submit": True})

		else:
			return "#########"

	else:
		u_form = UserProfileForm()
		return render(request, "recruiter_app/userprofileform.html", {"u_form": u_form, "successful_submit": False})


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
			return render(request,"recruiter_app/job_detail.html",context)  # return page after posting a new job
			pass
		else:
			pass
		pass
	else:
		form = JobCreationForm()
		return render(request, "recruiter_app/createjob.html", {"form": form})
		pass


@login_required
def applytojob(request, pk):
	job = Job.objects.get(pk=pk)

	# If User has already applied redirect User to already applied page.
	if request.user in job.applied_by.all():
		return render(request, "recruiter_app/apllication_done_already.html")

	# If User has not applied
	else:
		job.applied_by.add(request.user)
		# job.save()
		n_applications = job.applied_by.count()
		context = {  # Sending number of application to that job in the context
			"n_applications": n_applications
		}
		return render(request, "recruiter_app/application_done.html", context)


@login_required
def removeapplication(request, pk):
	job = Job.objects.get(pk=pk)

	# Validate if the User has applied in the first place
	if request.user not in job.applied_by.all():
		return render(request, "recruiter_app/application_not_done.html")

	# If the User has applied to the job, we can remove the application
	else:
		job.applied_by.remove(request.user)
		n_applications = job.applied_by.count()
		context = {  # Sending number of application to that job in the context
			"n_applications": n_applications
		}
		return render(request, "recruiter/application_removed.html", context)

@login_required
def remove(request,pk):
	can=ApplicantUserProfile.objects.get(pk=pk)
	user=request.user
	user.shortlist_can.remove(can)
	return render(request, "recruiter_app/remove_from_shortlist.html")


@login_required
def posted_jobs(request):
	"""
	View to fetch and display the list of jobs posted by a recruiter.
	"""
	jobs = request.user.jobs.all()
	context = {
		"jobs": jobs,
		"count": len(jobs),
	}

	return render(request, "recruiter_app/posted_jobs.html", context)
@login_required
def applicants(request,pk):
	job = Job.objects.get(pk=pk)
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

	context={
		"applicants":q,
		"applied_candidates":p,
        "job":job
	}
	return render(request, "recruiter_app/view_applicants.html", context)

def job_detail(request, pk=None):
    job = Job.objects.get(pk=pk)
    result = job.job_requirements
    mn = ApplicantUserProfile.objects.all()
    oo = ApplicantUserProfile.objects.none()
    perk =[]
    if (job.cert == True):
        perk.append("Certification")
    if (job.lor == True):
        perk.append("Letter Of Reccomendation")
    if (job.wh == True):
        perk.append("Work from Home")
    if (job.other):
        perk.append(job.other)
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
            'perks':perk
        }
    context['job'] = job

    return render(request, "recruiter_app/job_detail.html", context)



class Update_job(UpdateView):
	model=Job
	fields = ("primary_profile", "working_hour",
			  "notice_period",  "industry_type", "job_title", "job_info", 'job_vacancies',
			  "pincode", "exp_req", "cert_req", "types_of_job", "education_quali", "job_salary", "maximum",
			  "minimum", "other", "immediately",
			  "job_city", "state", "start_date", "job_requirements", "cert", "lor", "wh", "others")
	template_name = 'recruiter_app/createjob.html'


	def form_valid(self, form):
		form.instance.posted_by = self.request.user
		return super().form_valid(form)

def delete_job(request, pk):
	#model = Job
	#success_url = 'recruiter_app/posted_jobs.html'
    #k=6
    #prof="50%"
    #emp = Job.objects.get(pk=id)
   # emp.delete()
   # return render(request, "recruiter_app/posted_jobs.html")
    context = {}
    obj = get_object_or_404(Job, id=pk)
    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/recruiter/posted-jobs/")

    return render(request, "recruiter_app/posted_jobs.html", context)
k=""
prof=""
@login_required
def profile(request,pk):
	global k,prof

	user = ProfcessUser.objects.get(id=pk)
	try:
		UserUpdateForm(instance=request.user.recruiteruserprofile)
	except ObjectDoesNotExist:
		return redirect("recruiter:create_recruiter_profile")
	u_form= UserUpdateForm(instance=request.user.recruiteruserprofile)
	if request.method == "POST":
		u_form=UserUpdateForm(request.POST,instance=request.user.recruiteruserprofile)
		if u_form.is_valid():
			u_form.save()
			return render(request, "recruiter_app/userprofileform.html", {"u_form": u_form, "successful_submit": True})
	else:
		u_form = UserUpdateForm(instance=request.user.recruiteruserprofile)
	context = {
		'u_form': u_form,
		'prof': prof,
		"successful_submit": False
	}
	prof = "50%"
	k = 6

	return render(request, 'recruiter_app/userprofileform.html', context)


@login_required
def my_candidates(request):
	"""
	View to fetch and display the list of jobs posted by a recruiter.
	"""
	jobs = request.user.jobs.all()

	context = {
		"jobs": jobs,
		"count": len(jobs),
	}
	return render(request, "recruiter_app/my_candidates.html", context)
def search_candidates(request):
    m = ApplicantUserProfile.objects.all()
    page_number = request.GET.get('page')
    posted = request.GET.get('posted', False)
    if (request.user.paid_recruiter == False):
        paid = False
    else:
        paid = True
    query = ""
    location = ""
    context = {}
    if request.GET and posted==False:
        query = request.GET.get('q','')
        location = request.GET.get('l','')

        if query is None or location is not None:
            lookups = Q(location__icontains=location)
            m = ApplicantUserProfile.objects.filter(lookups).distinct()
            can = request.user.shortlist_can.all()
            if (request.user.paid_recruiter == False):
                m = m[:11]
            paginator = Paginator(m, 10)
            m = paginator.get_page(page_number)
            context['q']=query
            context['l']=location
            context['m']=m
            context['can']=can
            context['paid'] = paid

            return render(request, "recruiter_app/search_candidates.html", context)

        else:
            context = {
                'query': str(query)
            }
            m = get_queryset(query)
            can = request.user.shortlist_can.all()
            if (request.user.paid_recruiter == False):
                m = m[:11]
            paginator = Paginator(m, 10)
            m = paginator.get_page(page_number)
            context = {
                'm': m,
                'can':can
            }
            context['q'] = query
            context['l'] = location
            context['paid'] = paid
            return render(request, "recruiter_app/search_candidates.html", context)
    if posted=='True':
        qual = request.GET.get('qual', '')
        pass1 = request.GET.get('pass1','Any')
        pass2 = request.GET.get('pass2','Any')
        perfrom = request.GET.get('perfrom','From')
        perto = request.GET.get('perto','To')
        cgpafrom = request.GET.get('cgpafrom','From')
        cgpato = request.GET.get('cgpato','To')
        expfrom = request.GET.get('expfrom','Any')
        expto = request.GET.get('expto','Any')
        salmin = request.GET.get('salmin','Any')
        salmax = request.GET.get('salmax','Any')
        des = request.GET.get('des','')
        comp = request.GET.get('comp','')
        clgname = request.GET.get('clgname','')
        preclg = request.GET.get('preclg','')
        gender = request.GET.get('gender','')
        rate = request.GET.get('rate','')
        lang = request.GET.get('lang','')
        jtype = request.GET.get('jtype','')
        if qual:
            m = m.filter(Q(school_degree__icontains=qual))
            context['qual'] = qual
        if pass1 != 'Any':
            m = m.filter(Q(end_school__gte=pass1))
            context['pass1'] = pass1
        if pass2 != 'Any':
            m = m.filter(Q(end_school__lte=pass2))
            context['pass2'] = pass2
        # if perfrom != 'From':                       #Note: This commented code will be implemented when appropriate columns are added in applicant sideto take this information.
        #     m = m.filter(Q(percentage__gte=perfrom))
        #     context['perfrom'] = perfrom
        # if perto != 'To':
        #     m = m.filter(Q(percentage__lte=perto))
        #     context['perto'] = perto
        # if cgpafrom != 'From':
        #     m = m.filter(Q(cgpa__gte=cgpafrom))
        #     context['cgpafrom'] = cgpafrom
        # if cgpato != 'To':
        #     m = m.filter(Q(cgpa__lte=cgpato))
        #     context['cgpato'] = cgpato
        # if expfrom != 'Any':
        #     m = m.filter(Q(exp__gte=expfrom))
        #     context['expfrom'] = expfrom
        # if expto != 'Any':
        #     m = m.filter(Q(exp_lte=expto))
        #     context['expto'] = expto
        # if salmax != 'Any':
        #     m = m.filter(Q(sal__lte=salmax))
        #     context['salmax'] = salmax
        # if salmin != 'Any':
        #     m = m.filter(Q(sal__gte=salmin))
        #     context['salmin'] = salmin
        if des:
            m = m.filter(Q(experience_title__icontains=des))
            context['des'] = des
        if comp:
            m = m.filter(Q(company_name__icontains=comp))
            context['comp'] = comp
        if clgname:
            m = m.filter(Q(start_school__icontains=clgname))
            context['clgname'] = clgname
        if preclg:
            m = m.filter(Q(preclg__icontains=preclg))
            context['preclg'] = preclg
        if gender:
            m = m.filter(Q(gender__icontains=gender))
            context['gender'] = gender
        # if rate !='Select+English+Rating':
        #     m = m.filter(Q(rate__icontains=rate))
        # if lang!= 'Select+Language':
        #     m = m.filter(Q(lang__icontains=lang))
        # if jtype != 'Select+Job+Type':
        #     m = m.filter(Q(description__icontains=jtype))
        can = request.user.shortlist_can.all()
        if (request.user.paid_recruiter == False):
            m = m[:11]
        paginator = Paginator(m, 10)
        m = paginator.get_page(page_number)
        context['m'] = m
        context['can'] = can
        context['post_req'] = True
        context['paid'] = paid
        return render(request, "recruiter_app/search_candidates.html", context)
    if request.POST:
        qual = request.POST['qual']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        perfrom = request.POST['perfrom']
        perto = request.POST['perto']
        cgpafrom = request.POST['cgpafrom']
        cgpato = request.POST['cgpato']
        expfrom = request.POST['expfrom']
        expto = request.POST['expto']
        salmin = request.POST['salmin']
        salmax = request.POST['salmax']
        des = request.POST['des']
        comp = request.POST['comp']
        clgname = request.POST['clgname']
        preclg = request.POST['preclg']
        gender = request.POST.get('gender')
        rate = request.POST['rate']
        lang = request.POST['lang']
        jtype = request.POST['jtype']
        if qual:
            m = m.filter(Q(school_degree__icontains=qual))
            context['qual']=qual
        if pass1 != 'Any':
            m = m.filter(Q(end_school__gte=pass1))
            context['pass1']=pass1
        if pass2 !='Any':
            m = m.filter(Q(end_school__lte=pass2))
            context['pass2']=pass2
        if perfrom != 'From':
            m = m.filter(Q(percentage__gte=perfrom))
            context['perfrom']=perfrom
        if perto!='To':
            m = m.filter(Q(percentage__lte=perto))
            context['perto']=perto
        if cgpafrom != 'From':
            m = m.filter(Q(cgpa__gte=cgpafrom))
            context['cgpafrom']=cgpafrom
        if cgpato != 'To':
            m = m.filter(Q(cgpa__lte=cgpato))
            context['cgpato']=cgpato
        if expfrom != 'Any':
            m = m.filter(Q(exp__gte=expfrom))
            context['expfrom']=expfrom
        if expto != 'Any':
            m = m.filter(Q(exp_lte=expto))
            context['expto']=expto
        if salmax != 'Any':
            m = m.filter(Q(sal__lte=salmax))
            context['salmax']=salmax
        if salmin != 'Any':
            m = m.filter(Q(sal__gte=salmin))
            context['salmin']=salmin
        if  des:
            m = m.filter(Q(experience_title__icontains=des))
            context['des']=des
        if comp:
            m = m.filter(Q(company_name__icontains=comp))
            context['comp']=comp
        if clgname:
            m = m.filter(Q(start_school__icontains=clgname))
            context['clgname']=clgname
        if preclg:
            m = m.filter(Q(preclg__icontains=preclg))
            context['preclg'] = preclg
        if gender:
            m = m.filter(Q(gender__icontains=gender))
            context['gender'] = gender
        # if rate !='Select+English+Rating':
        #     m = m.filter(Q(rate__icontains=rate))
        # if lang!= 'Select+Language':
        #     m = m.filter(Q(lang__icontains=lang))
        # if jtype != 'Select+Job+Type':
        #     m = m.filter(Q(description__icontains=jtype))
        can = request.user.shortlist_can.all()
        if (request.user.paid_recruiter == False):
            m = m[:11]
        paginator = Paginator(m, 10)
        m = paginator.get_page(page_number)
        context['m']=m
        context['can']=can
        context['post_req']=True
        context['paid'] = paid
        return render(request, "recruiter_app/search_candidates.html", context)
    m = get_queryset(query)
    can = request.user.shortlist_can.all()
    if (request.user.paid_recruiter == False):
        m = m[:11]

    paginator = Paginator(m, 10)
    m = paginator.get_page(page_number)
    context = {
        'm': m,
        'can':can,
        'paid':paid
    }
    return render(request, "recruiter_app/search_candidates.html", context)


def get_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for ji in queries:
        candidates = ApplicantUserProfile.objects.filter(
            Q(skill_info__icontains=ji) |
            Q(description__icontains=ji) |
            Q(industry__icontains=ji)
        ).distinct()
        for can in candidates:
            queryset.append(can)
    return list(set(queryset))

def job_matching(request, pk=None):
    job = Job.objects.get(pk=pk)
    result = job.job_requirements
    mn=ApplicantUserProfile.objects.all()
    oo=ApplicantUserProfile.objects.none()
    z=[]
    for mm in mn:
        jk=mm.skill_info
        for x in result:
            for y in jk:
                if x==y:
                    z.append(mm.user)
    for ui in z:
            i=ApplicantUserProfile.objects.filter(user=ui)
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
			'count1':len(p),
			'qs1':p,

    }
    context['job'] = job
    return render(request, "recruiter_app/job_matching.html", context)

#def load_cities(request):
 #   states = State.objects.all()
  #  job=JobCreationForm()
   # state = request.GET.get('state')
    #from django.shortcuts import get_object_or_404

    #state = get_object_or_404(State, s_name=state)
    #state_id = state.id
    #cities = City.objects.filter(state_id=state_id).order_by('c_name')
    #return render(request, "recruiter_app/cities_filter.html", {'cities': cities})
    # return render(request, "recruiter_app/view_plans.html")


def applicant_detail(request, pk=None):
	context = {}
	applicantuserprofile = ApplicantUserProfile.objects.get(pk=pk)
	context['applicantuserprofile'] = applicantuserprofile
	return render(request, "recruiter_app/applicant_detail.html", context)


@login_required
def can(request, pk=None):
    context = {}
    user = request.user
    can = ApplicantUserProfile.objects.get(pk=pk)
    context['can'] = can
    if can in user.shortlist_can.all():
        context = {
            'can': user.shortlist_can.all()
        }

        return render(request, "recruiter_app/thanku.html", context)
    user.shortlist_can.add(can)

    return redirect(request.META['HTTP_REFERER'])


@login_required
def job_can(request, pk=None, mk=None):
    context = {}
    user = request.user
    can = ApplicantUserProfile.objects.get(pk=pk)
    context['can'] = can
    if can in user.shortlist_can.all():
        context = {
            'can': user.shortlist_can.all()
        }

        return render(request, "recruiter_app/thanku.html", context)
    user.shortlist_can.add(can)
    job = Job.objects.get(pk=mk)

    can.job_for_which_shortlisted = job.job_title
    can.save()


    return redirect(request.META['HTTP_REFERER'])


@login_required
def alreadycan(request):
	user=request.user
	context = {
		'can': user.shortlist_can.all()
	}
	return render(request, "recruiter_app/applicationdonealready.html", context)
@login_required
def dashboard(request):
	return render(request,"recruiter_app/dashboard.html")
@login_required
def pricing(request):
	return render(request,"recruiter_app/view_plans.html")
@login_required
def purchase_plan(request):
	return render(request,"recruiter_app/purchase_plan.html")
@login_required
def campus_hiring(request):
	return render(request,"recruiter_app/campus_hiring.html")



@login_required
def assessments(request):
	return render(request,"recruiter_app/assessments.html")



@login_required
def add_a_blog(request):
	return render(request,"recruiter_app/add_a_blog.html")

@login_required
def recruiter_blog(request):
	return render(request,"recruiter_app/recruiter_blog.html")
@login_required
def upload_pic(request, pk):
    user = ProfcessUser.objects.get(id=pk)
    try:
        form = PicForm(instance=request.user.recruiteruserprofile)
        if request.method == "POST":
            form = PicForm(request.POST, request.FILES, instance=request.user.recruiteruserprofile)
            if form.is_valid():
                form.save()
                return render(request, "recruiter_app/update_success.html")

        args = {'form': form}
        return render(request, 'recruiter_app/uploadpic.html', args)
    except ObjectDoesNotExist:
        return render(request, 'recruiter_app/fill_application.html')


@login_required
def delete_pic(request,pk):
	# user = ProfcessUser.objects.get(id=pk)
	# context={}
	# obj = get_object_or_404(RecruiterUserProfile, pk=pk)
	#
	# obj.profile_pic.delete()
    try:
        form = PicForm(instance=request.user.recruiteruserprofile)
        request.user.recruiteruserprofile.profile_pic.delete()
        return render(request, "recruiter_app/update_success.html")
    except ObjectDoesNotExist:
        return render(request, 'recruiter_app/fill_application.html')

	# return render(request, "recruiter_app/update_success.html", context)
@login_required
def cart_summary(request):
	user=request.user
	p = len(user.shortlist_can.all()) *2000;
	total = p+400-100;
	context = {
		'can': user.shortlist_can.all(),
		'count':len(user.shortlist_can.all()),
		'price': p,
		'total':total
	}
	return render(request, 'recruiter_app/cart_summary.html',context)

payu_config = settings.PAYU_CONFIG
merchant_key = payu_config.get('merchant_key')
merchant_salt = payu_config.get('merchant_salt')
surl = payu_config.get('success_url')
furl = payu_config.get('failure_url')
mode = payu_config.get('mode')
payu = Payu(merchant_key, merchant_salt, surl, furl, mode)

def payu_payment(request):
	user = request.user
	p = len(user.shortlist_can.all()) * 2000;
	total = p + 400 + 100;
	data = {k: v[0] for k, v in dict(request.POST).items()}
	#data.pop('csrfmiddlewaretoken')
	# The dictionary data  should be contains following details
	data = {
		'amount': total,
		'firstname': request.user.first_name,
		'email': request.user.email,
		'phone': request.user.recruiteruserprofile.phone,
		'productinfo': 'profcess',
		'lastname': request.user.recruiteruserprofile.last_name,
		'address1': request.user.recruiteruserprofile.location,
		'address2': 'test', 'city': request.user.recruiteruserprofile.state,
		'state': request.user.recruiteruserprofile.state, 'country': request.user.recruiteruserprofile.country,
		'zipcode': 'tes', 'udf1': '',
		'udf2': '', 'udf3': '', 'udf4': '', 'udf5': ''

	}
	data.update({'txnid': "xyz"})
	# No Transactio ID's, Create new with paywix, it's not mandatory Create your own
	# Create transaction Id with payu and verify with table it's not existed
	payu_data = payu.transaction(**data)
	return render(request, 'recruiter_app/pay_payment.html', {"posted": payu_data})

def success(request):
    data = {k: v[0] for k, v in dict(request.POST).items()}
    response = payu.verify_transaction(data)
    return JsonResponse(response)
@csrf_exempt
def failure(request):
    data = {k: v[0] for k, v in dict(request.POST).items()}
    response = payu.verify_transaction(data)
    return JsonResponse(response)


@login_required
def paypal_payment(request):
	user = request.user
	p = len(user.shortlist_can.all()) * 2000;
	total = p + 400 + 100;
	context = {
		'can': user.shortlist_can.all(),
		'count': len(user.shortlist_can.all()),
		'price': p,
		'total': total
	}
	return render(request, 'recruiter_app/paypal_payment.html', context)

def download(request, path):
    file_path= os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path,'rb') as fh:
            response=HttpResponse(fh.read(),content_type="application/profile_resume")
            response['Content-Disposition']='inline; filename='+os.path.basename(file_path)
            return response

    raise Http404

def plan(request):
	request.user.paid_recruiter=True
	request.user.save()
	return render(request, 'recruiter_app/plan.html')

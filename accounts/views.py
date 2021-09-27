import csv, io
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy
from django.views.generic import CreateView, View
from .forms import RecruiterCreationForm, ApplicantCreationForm,CollegeCreationForm,EmailForm,CFormFooter,GeeksForm,Form1
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_text,DjangoUnicodeDecodeError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from .models import ProfcessUser
from django.contrib import messages
from django.http import HttpResponse
from django.core.mail import send_mail
from .token import activation_token
from applicant_app.models import ApplicantUserProfile
from recruiter_app.forms import UserProfileForm,UserUpdateForm
from django.core.exceptions import ObjectDoesNotExist
from applicant_app.forms import UserProfileForm,UserProfileUpdationForm
from college_app.forms import UserUpdateFormCollege,UserProfileForm,CollegeUserProfile
from social.models import MyProfile

# Create your views here.
def index(request):
    p=ProfcessUser.objects.all()
    if request.user in p:
        if request.user.usertype=='Recruiter':
            if request.user.activated == False:
                messages.info(request, "You have not confirmed your email address yet."
                                       " If you cannot find your confirmation email anymore, send yourself a new one here.")
                set=True
            '''if request.method == 'POST':
                u_form = UserUpdateForm(request.POST, instance=request.user)
                if u_form.is_valid():
                    u_form.save()
                    return render(request,'recruiter_app/update_success.html')
            else:
                u_form = UserUpdateForm(instance=request.user)
            context = {
                'u_form': u_form,
            }
            return render(request, 'recruiter_app/profile.html', context)'''
            try:
                UserUpdateForm(instance=request.user.recruiteruserprofile)
            except ObjectDoesNotExist:
                return redirect("recruiter:home")
            form = UserUpdateForm(instance=request.user.recruiteruserprofile)
            args = {'form': form}
            return redirect("recruiter:home")
        elif request.user.usertype=='Applicant':
            if request.user.activated == False:
                messages.info(request, "You have not confirmed your email address yet. "
                                       "If you cannot find your confirmation email anymore, send yourself a new one here.")
                set = True
            try:
                UserProfileUpdationForm(instance=request.user.applicantuserprofile)
            except ObjectDoesNotExist:
                return redirect("applicant:jobs_list")
            form = UserProfileUpdationForm(instance=request.user.applicantuserprofile)
            args = {'form': form}
            return redirect("applicant:edit_profile", pk=request.user.pk)#render(request, "applicant_app/userprofileform.html", args)
        elif request.user.usertype=='College':
            if request.user.activated == False:
                messages.info(request, "You have not confirmed your email address yet."
                                       " If you cannot find your confirmation email anymore, send yourself a new one here.")
                set = True
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
        else:
            return redirect("accounts:signup")
    else:
        return render(request, "index.html")
def about(request):
    return render(request, "about.html")
    pass

def contact(request):
    return render(request, "contact.html")
    pass

def Fcontact(request):
    return render(request, "base.html")

def findJob(request):
    return render(request, "findJob.html")
    pass
def careerAdvice(request):
    return render(request, "careerAdvice.html")
    pass
def findATalent(request):
    return render(request, "findATalent.html")
    pass
def services(request):
    return render(request, "services.html")
    pass
def recruiter_signup(request):
        form = RecruiterCreationForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            site = get_current_site(request)
            mail_subject = 'Confirmation message'
            message = render_to_string('registration/activate.html', {
                'user': user,
                'domain': site.domain,
                'uid': user.pk,
                'token': activation_token.make_token(user)
            })
            to_email = form.cleaned_data.get('email')
            to_list = [to_email]
            from_email = settings.EMAIL_HOST_USER
            send_mail(mail_subject, message, from_email, to_list, fail_silently=True)


            new_user = authenticate(username=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1'],
                                    )

            fid = MyProfile.objects.create(user_id=user)

            login(request, new_user)
            return redirect('accounts:index')
        return render(request, 'registration/signup.html', {"form": form})
def activate(request,uid,token):
    request.user.activated=True
    request.user.save()
    return redirect('accounts:index')

def email_form(request):
        if request.method == "POST":
            eform = EmailForm(request.POST or None)
            if eform.is_valid():
                p = ProfcessUser.objects.get(pk=request.user.pk)
                user = eform.save(commit=False)
                site = get_current_site(request)
                mail_subject = 'Confirmation message'
                message = render_to_string('registration/activate.html', {
                    'user': user,
                    'domain': site.domain,
                    'uid': user.pk,
                    'token': activation_token.make_token(user)
                })
                to_email = eform.cleaned_data.get('verified_email')
                p.verified_email = to_email
                p.save()
                to_list = [to_email]
                from_email = settings.EMAIL_HOST_USER
                send_mail(mail_subject, message, from_email, to_list, fail_silently=True)
                user.verified_email = to_email
                return redirect('accounts:index')
                pass
            else:
                eform = EmailForm(request.POST or None)
                return render(request, 'registration/email_form.html', {"form": eform})
                pass
        else:
            eform = EmailForm(request.POST or None)
            return render(request, 'registration/email_form.html', {"form": eform})
            pass



def showprivacy(request):
    return render(request,'registration/privacy.html')

def showterms(request):
    return render(request,'registration/terms.html')

def dashboard(request):
    return render(request,'dashboard.html')

def ApplicantSignUp(request):
        form = ApplicantCreationForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            site = get_current_site(request)
            mail_subject = 'Confirmation message'
            message = render_to_string('registration/activate.html', {
                'user': user,
                'domain': site.domain,
                'uid': user.pk,
                'token': activation_token.make_token(user)
            })
            to_email = form.cleaned_data.get('email')
            to_list = [to_email]
            from_email = settings.EMAIL_HOST_USER
            send_mail(mail_subject, message, from_email, to_list, fail_silently=True)

            new_user = authenticate(username=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1'],
                                    )

            fid = MyProfile.objects.create(user_id=user)

            login(request, new_user)
            return redirect('accounts:index')
        return render(request, 'registration/signup.html', {"form": form})

def college_signup(request):
    form = CollegeCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.save()
        site = get_current_site(request)
        mail_subject = 'Confirmation message'
        message = render_to_string('registration/activate.html', {
            'user': user,
            'domain': site.domain,
            'uid': user.pk,
            'token': activation_token.make_token(user)
        })
        to_email = form.cleaned_data.get('email')
        to_list = [to_email]
        from_email = settings.EMAIL_HOST_USER
        send_mail(mail_subject, message, from_email, to_list, fail_silently=True)

        new_user = authenticate(username=form.cleaned_data['email'],
                                password=form.cleaned_data['password1'],
                                )
        fid = MyProfile.objects.create(user_id=user)

        login(request, new_user)
        return redirect('accounts:index')
    return render(request, 'registration/signup.html', {"form": form})

def get_context(request):
    if (request.user.is_authenticated):
        context=ApplicantUserProfile.objects.filter(user=request.user).values()[0]
        #conversion=model_to_dict(reqfield)
        context.pop('id')
        context.pop('user_id')
        return context
def profile_upload(request):
    # declaring template
    template = "accounts/profile_upload.html"
    data = ProfcessUser.objects.all()
# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Order of the CSV should be username, email, password, confirm password, first name, last name, company name, phone',
        'profiles': data
              }

    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')

    io_string = io.StringIO(data_set)
    next(io_string)
    name_exists = []
    email_exists= []
    for column in csv.reader(io_string, delimiter=',', quotechar='"'):
        name = column[1]
        email = column[2]
        if ProfcessUser.objects.filter(username=name).exists():
            name_exists.append(name)
            continue
        if ProfcessUser.objects.filter(email=email).exists():
            email_exists.append(email)
            continue
        user_obj, created = ProfcessUser.objects.update_or_create(
        username=column[1],
        email=column[2],
        usertype = column[3],
        password=column[4],
        first_name = column[6],
        last_name = column[7]
        )


        data2 = ApplicantUserProfile.objects.all()
        skill_infos = column[10]
        skills = skill_infos.split(',')
        lst = []
        for s in skills:
            lst.append(s.strip())
        applicant_user, created = ApplicantUserProfile.objects.update_or_create(
            user = user_obj,
            first_name = column[6],
            last_name = column[7],
            contact_information = column[8],
            location = column[9],
            school_degree = column[11],
            skill_info = lst
        )


    context = {'user_exists':name_exists,'email_exists':email_exists}
    return render(request, template, context)

def SignUp1(request):
    p=ProfcessUser.objects.all()
    if request.user in p:
        ProfcessUser.objects.filter(email=request.user).delete()
    uu=GeeksForm(request.POST or None)
    form = Form1(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False)
        user.save()
        site = get_current_site(request)
        mail_subject = 'Confirmation message'
        message = render_to_string('registration/activate.html', {
            'user': user,
            'domain': site.domain,
            'uid': user.pk,
            'token': activation_token.make_token(user)
        })

        to_email = form.cleaned_data.get('email')
        to_list = [to_email]
        from_email = settings.EMAIL_HOST_USER
        send_mail(mail_subject, message, from_email, to_list, fail_silently=True)

        new_user = authenticate(username=form.cleaned_data['email'],
                                password=form.cleaned_data['password1'],
                                )
        fid = MyProfile.objects.create(user_id=user)
        login(request, new_user)
        k=request.user.usertype
        #if k=='Applicant':
        #Article.objects.filter(category="web")
        return redirect('accounts:login')
    return render(request, 'registration/signup1.html', {"form": form, "uu":uu})

from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib.auth import get_user_model



def password_reset_request(request):

    if request.method == "POST":

        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            User = get_user_model()
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "accounts/password_reset_email"
                    c = {
                    "email":user.email,
                    'domain':'www.profcess.com',
                    'site_name': 'Website',
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "user": user,
                    'token': default_token_generator.make_token(user),
                    'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, settings.EMAIL_HOST_USER , [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')

                    messages.success(request, 'A message with reset password instructions has been sent to your inbox.')
                    return redirect ("/password_reset/done/")
        messages.error(request, 'An invalid email has been entered.')
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="accounts/password_reset.html", context={"password_reset_form":password_reset_form})













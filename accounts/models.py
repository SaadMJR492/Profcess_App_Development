from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.base_user import BaseUserManager
from django.contrib import auth
from phonenumber_field.modelfields import PhoneNumberField
from applicant_app.models import ApplicantUserProfile
can=ApplicantUserProfile

class ProfcessUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        # usertype = usertype
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        # extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('usertype', 'Developer')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        # if extra_fields.get('is_admin') is not True:
        #     raise ValueError('Superuser must have is_admin=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get('usertype') != "Developer" :
            raise ValueError('Superuser must have usertype=Developer')

        return self._create_user(username, email, password, **extra_fields)

    def with_perm(self, perm, is_active=True, include_superusers=True, backend=None, obj=None):
        if backend is None:
            backends = auth._get_backends(return_tuples=True)
            if len(backends) == 1:
                backend, _ = backends[0]
            else:
                raise ValueError(
                    'You have multiple authentication backends configured and '
                    'therefore must provide the `backend` argument.'
                )
        elif not isinstance(backend, str):
            raise TypeError(
                'backend must be a dotted import path string (got %r).'
                % backend
            )
        else:
            backend = auth.load_backend(backend)
        if hasattr(backend, 'with_perm'):
            return backend.with_perm(
                perm,
                is_active=is_active,
                include_superusers=include_superusers,
                obj=obj,
            )
        return self.none()


class ProfcessUser(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    email = models.EmailField(
        _('email address'), 
        unique=True,
        error_messages={
            'unique': _("A user with that Email already exists."),
        },
    )
    verified_email = models.EmailField(blank=True)

    USERTYPE_CHOICES=[
        ("Recruiter", "Recruiter"),
        ("Applicant", "Applicant"),
        ("College", "College"),
        ("Developer", "Developer"),
    ]
    usertype = models.CharField(
        _("usertype"),
        max_length=15,
        choices=USERTYPE_CHOICES,
        blank=True
    )
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    phone = PhoneNumberField(region="IN",default="")
    company_name = models.CharField(_('company name'), max_length=30, blank=True)
    paid_recruiter=models.BooleanField(default=False)
    college_name = models.CharField(_('college name'), max_length=30, blank=True)
    college_name_stu = models.CharField(_('College name'), max_length=30, blank=True)

    #designation = models.CharField(_('designation'), max_length=30, blank=True)
    #location = models.CharField(_('location'), max_length=130, blank=True)
    #url_of_company = models.CharField(_('url of company'), max_length=230, blank=True)
    url_of_college = models.CharField(_('url of college'), max_length=230, blank=True)

    #why_join_us = models.CharField(_('why join us'), max_length=530, blank=True)
    #company_description = models.CharField(_('companydescription'), max_length=530, blank=True)
    college_description = models.CharField(_('collegedescription'), max_length=530, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    activated = models.BooleanField(
        default=False
    )

    uname=models.CharField(max_length=530,blank=False,default="")
    mail=models.EmailField(blank=False,default="")
    telephone=PhoneNumberField(region="IN",default="")
    message=models.CharField(max_length=530,blank=False,default="")
    shortlist_can=models.ManyToManyField(
        can,
        related_name="shortlist_can",
        blank=True)
    
    objects = ProfcessUserManager()


    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]
    is_termnsandconditions=models.BooleanField("Agree to terms and Conditions",default=False)

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)
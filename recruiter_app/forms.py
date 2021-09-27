from django import forms
from multiselectfield import MultiSelectFormField
from django_select2.forms import Select2MultipleWidget

from .models import RecruiterUserProfile, Job, UserData



class UserProfileForm(forms.ModelForm):
	# first_name = forms.CharField(max_length=140, widget=forms.TextInput(attrs={'class': 'form-control input-lg'}))
	# last_name = forms.CharField(max_length=140, widget=forms.TextInput(attrs={'class': 'form-control input-lg'}))
	# location = forms.CharField(max_length=140, widget=forms.TextInput(attrs={'class': 'form-control'}))
	# designation = forms.CharField(max_length=140, widget=forms.TextInput(attrs={'class': 'form-control'}))
	# company_name = forms.CharField(max_length=140, widget=forms.TextInput(attrs={'class': 'form-control'}))
	# Url_of_company = forms.CharField(max_length=140, widget=forms.TextInput(attrs={'class': 'form-control'}))
	# why_join_us = forms.CharField(max_length=540, widget=forms.TextInput(attrs={'class': 'form-control'}))
	# # cell = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
	# # HR_email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	# company_description = forms.CharField(max_length=540, widget=forms.TextInput(attrs={'class': 'form-control'}))

	class Meta:
		model = RecruiterUserProfile
		fields = (
		"first_name", "last_name", "username", "email", "phone", "country", "state", "designation", "company_name",
		"company_email", "Url_of_company", "why_join_us", "company_description", "location")

	pass


class JobCreationForm(forms.ModelForm):

	class Meta:
		model = Job
		#widgets = {
		#	'types_of_job': forms.RadioSelect(),
		#	'start_date': forms.RadioSelect(),
		#	'perks':forms.RadioSelect(),}

		fields = ("primary_profile", "working_hour",
				  "notice_period", "industry_type", "job_title", "job_info", 'job_vacancies',
				  "pincode", "exp_req", "cert_req", "types_of_job", "education_quali", "job_salary", "maximum",
				  "minimum", "other",
			"job_city", "state", "start_date", "job_requirements", "cert", "lor", "wh", "others", "immediately")
		widgets = {
			'job_title': forms.TextInput(attrs={'placeholder': 'UX/UI Designer'}),

			'notice_period': forms.Select(attrs={'class':'select-css'}),
			'primary_profile': forms.Select(attrs={'class':'select-css',}),
			'state': forms.Select(attrs={'class': 'select-css'}),
			'working_hour': forms.Select(attrs={'class': 'select-css'}),
			'industry_type': forms.Select(attrs={'class': 'select-css'}),
			'pincode': forms.TextInput(attrs={'placeholder': '123456'}),
			'job_vacancies': forms.Select(attrs={'class':'select-css'}),
			'minimum': forms.TextInput(attrs={'placeholder': '   20,000            CTC'}),
			'maximum': forms.TextInput(attrs={'placeholder': '   40,000            CTC'}),
			'types_of_job':forms.Select(attrs={'class': 'select-css'}),
			'cert_req':forms.TextInput(attrs={'placeholder': 'e.g.ABC'}),
			'exp_req': forms.Select(attrs={'class': 'select-css'}),
		}
	#def __init__(self, *args, **kwargs):
	#	super().__init__(*args, **kwargs)
	#	self.fields['city'].queryset = City.objects.none()

	#	if 'state' in self.data:
	#		try:
	#			state_id = int(self.data.get('state'))
	#			self.fields['city'].queryset = City.objects.filter(state_id=state_id).order_by('c_name')
	#		except (ValueError, TypeError):
	#			pass  # invalid input from the client; ignore and fallback to empty City queryset
	#	elif self.instance.pk:
	#		self.fields['city'].queryset = self.instance.state.city_set.order_by('c_name')



	#pass

class JobUpdationForm(forms.ModelForm):

	class Meta:
		model = Job
		fields = ("primary_profile", "working_hour",
				  "notice_period",  "industry_type", "job_title", "job_info", 'job_vacancies',
				  "pincode", "exp_req", "cert_req", "types_of_job", "education_quali", "job_salary", "maximum",
				  "minimum", "other", "state", "start_date", "job_requirements", "cert", "lor", "wh",
				  "others", "immediately","job_city")

	def save(self, commit=True):
		job = self.instance
		job.primary_profile = self.cleaned_data['primary_profile']
		job.cert_req = self.cleaned_data['cert_req']
		job.maximum = self.cleaned_data['maximum']
		job.minimum = self.cleaned_data['minimum']
		job.other = self.cleaned_data['other']

		job.job_vacancies =  self.cleaned_data['job_vacancies']
		job.notice_period = self.cleaned_data['notice_period']
		job.industry_type = self.cleaned_data['industry_type']
		job.job_title = self.cleaned_data['job_title']

		job.job_info = self.cleaned_data['job_info']
		job.types_of_job = self.cleaned_data['types_of_job']
		job.job_city = self.cleaned_data['job_city']
		job.state = self.cleaned_data['state']
		job.start_date = self.cleaned_data['start_date']
		job.job_requirements = self.cleaned_data['job_requirements']
		job.education_quali = self.cleaned_data['education_quali']
		job.exp_req = self.cleaned_data['exp_req']
		job.job_salary = self.cleaned_data['job_salary']
		job.cert = self.cleaned_data['cert']
		job.lor = self.cleaned_data['lor']
		job.wh = self.cleaned_data['wh']
		job.others = self.cleaned_data['others']
		job.immediately = self.cleaned_data['immediately']


		if commit:
			job.save()
		return job


class DetailUpdateForm(forms.ModelForm):
	class Meta:
		model = RecruiterUserProfile
		fields = ["first_name", "last_name", "username", "email", "phone", "country", "state", "designation",
				  "company_name", "company_email", "Url_of_company", "why_join_us", "company_description", "location"]



class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = RecruiterUserProfile
		fields = ["company_name", "designation", "location",
				  "Url_of_company", "why_join_us", "company_description", "state", "country",
				  "company_email"]  # 'username', 'email', "first_name", "last_name", "phone",


class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = UserData
		fields = ['token']

class PicForm(forms.ModelForm):

    class Meta:
        model = RecruiterUserProfile
        fields = ("profile_pic",)
    pass

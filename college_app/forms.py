from django import forms
from multiselectfield import MultiSelectFormField
from .models import CollegeUserProfile, Jobs


class UserProfileForm(forms.ModelForm):
	name = forms.CharField(max_length=140, widget=forms.TextInput(attrs={'class': 'form-control'}))
	location = forms.CharField(max_length=140, widget=forms.TextInput(attrs={'class': 'form-control'}))
	designation = forms.CharField(max_length=140, widget=forms.TextInput(attrs={'class': 'form-control'}))
	college_name = forms.CharField(max_length=140, widget=forms.TextInput(attrs={'class': 'form-control'}))
	Url_of_college = forms.CharField(max_length=140, widget=forms.TextInput(attrs={'class': 'form-control'}))
	why_join_us = forms.CharField(max_length=540, widget=forms.TextInput(attrs={'class': 'form-control'}))
	# cell = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
	# HR_email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	college_description = forms.CharField(max_length=540, widget=forms.TextInput(attrs={'class': 'form-control'}))

	class Meta:
		model = CollegeUserProfile
		fields = (
		"name", "location", "designation", "college_name", "Url_of_college", "why_join_us", "college_description")

	pass
class UserUpdateFormCollege(forms.ModelForm):
	email = forms.EmailField()
	class Meta:
		model = CollegeUserProfile
		fields = ["college_name", "designation", "location",
				  "url_of_college", "why_join_us", "college_description", ]#'username', 'email', "first_name", "last_name", "phone", 
class JobCreationForm(forms.ModelForm):
	#job_requirements = forms.MultipleChoiceField(choices=Job.SKILLS)

	class Meta:
		model = Jobs

		# widgets = {
		# 	'types_of_job': forms.RadioSelect(),
		# 	'start_date': forms.RadioSelect(),
		# 	'perks':forms.RadioSelect(),
		# }
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
		pass


class JobUpdationForm(forms.ModelForm):
	#job_requirements = forms.MultipleChoiceField(choices=Job.SKILLS)

	class Meta:
		model = Jobs
		# widgets = {
		# 	'types_of_job': forms.RadioSelect(),
		# 	'start_date': forms.RadioSelect(),
		# 	'perks':forms.RadioSelect(),
		# }
		fields = ("primary_profile", "functional_area", "job_role", "responsibility", "job_duration",
				  "notice_period", "essential_skills", "industry_type", "job_title", "job_vacancies", "job_info",
				  "pincode", "exp_req", "cert_req", "types_of_job", "education_quali", "job_salary", "maximum",
				  "minimum", "perks", "other",
				  "city", "state", "start_date", "job_requirements")

	def save(self, commit=True):
		job = self.instance
		job.primary_profile = self.cleaned_data['primary_profile']
		job.cert_req = self.cleaned_data['cert_req']
		job.maximum = self.cleaned_data['maximum']
		job.minimum = self.cleaned_data['minimum']
		job.other = self.cleaned_data['other']
		job.functional_area = self.cleaned_data['functional_area']
		job.job_role = self.cleaned_data['job_role']
		job.responsibility = self.cleaned_data['responsibility']
		job.notice_period = self.cleaned_data['notice_period']
		job.essential_skills = self.cleaned_data['essential_skills']
		job.industry_type = self.cleaned_data['industry_type']
		job.job_title = self.cleaned_data['job_title']
		job.job_vacancies = self.cleaned_data['job_vacancies']
		job.job_info = self.cleaned_data['job_info']
		job.types_of_job = self.cleaned_data['types_of_job']
		job.city = self.cleaned_data['city']
		job.state = self.cleaned_data['state']
		job.start_date = self.cleaned_data['start_date']
		job.job_requirements = self.cleaned_data['job_requirements']
		job.education_quali = self.cleaned_data['education_quali']
		job.exp_req = self.cleaned_data['exp_req']
		job.job_salary = self.cleaned_data['job_salary']
		job.perks = self.cleaned_data['perks']
		job.last_date = self.cleaned_data['last_date']
		if commit:
			job.save()
		return job


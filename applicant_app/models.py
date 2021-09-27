from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator
from multiselectfield import MultiSelectField
from Profcess_Dev.settings import AUTH_USER_MODEL
User = AUTH_USER_MODEL
from django.core.exceptions import ValidationError

# Create your models here.



class ApplicantUserProfile(models.Model):
    def validate(value):  # <-changed this
        filesize = value.size

        if filesize > 14000:
            raise ValidationError("Your file is too big. The maximum file size that can be uploaded is 13KB")
        else:
            return value  # <-to this

    def validate1(value):  # <-changed this
        filesize = value.size

        if filesize > 14000:
            raise ValidationError("Your file is too big. The maximum file size that can be uploaded is 13KB")
        else:
            return value  # <-to this

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={"usertype": "Applicant"},
        related_name="applicantuserprofile",
        null=True,)
    headline = models.CharField(blank=True, max_length=140)
    first_name = models.CharField(blank=True, max_length=140)
    last_name = models.CharField(blank=True, max_length=140)
    pheadline = models.CharField(blank=True, max_length=140)
    current_position = models.CharField(blank=True, max_length=140)
    education = models.CharField(blank=True, max_length=140)
    country_region = models.CharField(blank=True, max_length=140)
    location = models.CharField(blank=True, max_length=140)
    industry = models.CharField(blank=True, max_length=140)
    contact_information = models.CharField(blank=True, max_length=140)
    description = models.CharField(blank=True, max_length=25)
    school_name = models.CharField(blank=True, max_length=140)
    school_degree = models.CharField(blank=True, max_length=140)
    field_of_study = models.CharField(blank=True, max_length=140)
    location_of_school = models.CharField(blank=True, max_length=140)
    start_school = models.CharField(blank=True, max_length=140)
    end_school = models.CharField(blank=True, max_length=140)
    experience_title = models.CharField(blank=True, max_length=140)
    company_name = models.CharField(blank=True, max_length=140)
    company_city = models.CharField(blank=True, max_length=140)
    company_state = models.CharField(blank=True, max_length=140)
    start_company = models.CharField(blank=True, max_length=140)
    end_company = models.CharField(blank=True, max_length=140)
    area_of_expertise = models.CharField(blank=True, max_length=140)
    project_name = models.CharField(blank=True, max_length=140)
    start_project = models.CharField(blank=True, max_length=140)
    end_project = models.CharField(blank=True, max_length=140)
    project_creator = models.CharField(blank=True, max_length=140)
    associated_with = models.CharField(blank=True, max_length=140)
    project_url = models.CharField(blank=True, max_length=140)
    project_description = models.CharField(blank=True, max_length=140)
    accomplishment_title = models.CharField(blank=True, max_length=140)
    accomplishment_associated_with = models.CharField(blank=True, max_length=140)
    issuer = models.CharField(blank=True, max_length=140)
    issue_date = models.CharField(blank=True, max_length=140)
    accomplishment_description = models.CharField(blank=True, max_length=140)
    # SKILLS = []

    # file1 = open('static/skill/all_skills.txt', 'r', encoding="utf-8")
    # Lines = file1.readlines()

    # for line in Lines:
    #     SKILLS += [(str(line[:-1]), str(line[:-1]))]

    SKILLS = [
        ('A/B Testing', 'A/B Testing'),
        ('Abap', 'Abap'),
        ('Accounting', 'Accounting'),
        ('Active Listening', 'Active Listening'),
        ('Ada', 'Ada'),
        ('Adaptability', 'Adaptability'),
        ('Agile', 'Agile'),
        ('Agile Development', 'Agile Development'),
        ('Answering Phones', 'Answering Phones'),
        ('Artificial Intelligence', 'Artificial Intelligence'),
        ('Ballerina', 'Ballerina'),
        ('BASIC Alice', 'BASIC Alice'),
        ('Billing', 'Billing'),
        ('Blood Pressure Monitoring', 'Blood Pressure Monitoring'),
        ('Budgeting', 'Budgeting'),
        ('C', 'C'),
        ('C#', 'C#'),
        ('C++', 'C++'),
        ('CAD', 'CAD'),
        ('Calendar Management', 'Calendar Management'),
        ('Cashier Skills', 'Cashier Skills'),
        ('Clojure Elixir', 'Clojure Elixir'),
        ('Cloud Management', 'Cloud Management'),
        ('CMS Tools', 'CMS Tools'),
        ('Cobol', 'Cobol'),
        ('COBOL', 'COBOL'),
        ('Coding Java Script', 'Coding Java Script'),
        ('Collaboration', 'Collaboration'),
        ('Communication', 'Communication'),
        ('Computer Skills', 'Computer Skills'),
        ('Conflict Resolution', 'Conflict Resolution'),
        ('Contract Negotiation', 'Contract Negotiation'),
        ('CPC', 'CPC'),
        ('Creativity', 'Creativity'),
        ('Critical Thinking', 'Critical Thinking'),
        (
        'CRM Software (Salesforce, Hubspot, Zoho, Freshsales)', 'CRM Software (Salesforce, Hubspot, Zoho, Freshsales)'),
        ('CRO', 'CRO'),
        ('CSS', 'CSS'),
        ('Customer Needs Analysis', 'Customer Needs Analysis'),
        ('Customer Service', 'Customer Service'),
        ('Dart', 'Dart'),
        ('Data Entry', 'Data Entry'),
        ('Data Structures', 'Data Structures'),
        ('Data Visualization', 'Data Visualization'),
        ('Debugging', 'Debugging'),
        ('Decision Making', 'Decision Making'),
        ('Design', 'Design'),
        ('Digital marketing', 'Digital marketing'),
        ('Eiffel', 'Eiffel'),
        ('Electronic Heart Record (EHR)', 'Electronic Heart Record (EHR)'),
        ('Electronic Medical Record (EMR)', 'Electronic Medical Record (EMR)'),
        ('Elm', 'Elm'),
        ('Email Automation', 'Email Automation'),
        ('Email Marketing', 'Email Marketing'),
        ('Empathy', 'Empathy'),
        ('Erlang', 'Erlang'),
        ('Feature Definition', 'Feature Definition'),
        ('Financial Modelling', 'Financial Modelling'),
        ('Forecasting', 'Forecasting'),
        ('FORTRAN', 'FORTRAN'),
        ('Front-End & Back-End Development', 'Front-End & Back-End Development'),
        ('Glucose Checks', 'Glucose Checks'),
        ('Go (Golang)', 'Go (Golang)'),
        ('Graphic Design Skills', 'Graphic Design Skills'),
        ('Groovy Perl', 'Groovy Perl'),
        ('Haskell Delphi', 'Haskell Delphi'),
        ('Hygiene Assistance', 'Hygiene Assistance'),
        ('HTML', 'HTML'),
        ('Ideation Leadership', 'Ideation Leadership'),
        ('Increasing Customer Lifetime Value (CLV)', 'Increasing Customer Lifetime Value (CLV)'),
        ('Interpersonal Communication', 'Interpersonal Communication'),
        ('Java', 'Java'),
        ('JavaScript', 'JavaScript'),
        ('Julia', 'Julia'),
        ('Kotlin', 'Kotlin'),
        ('Lead Prospecting', 'Lead Prospecting'),
        ('Lead Qualification', 'Lead Qualification'),
        ('Leadership', 'Leadership'),
        ('Lean Manufacturing', 'Lean Manufacturing'),
        ('LISP', 'LISP'),
        ('Lua', 'Lua'),
        ('Machine Learning', 'Machine Learning'),
        ('Management', 'Management'),
        ('Managing Cross-Functional Teams', 'Managing Cross-Functional Teams'),
        ('MATLAB', 'MATLAB'),
        ('Medicine Administration', 'Medicine Administration'),
        ('Meditech', 'Meditech'),
        ('Meeting Facilitation', 'Meeting Facilitation'),
        ('MS Office', 'MS Office'),
        ('Negotiation', 'Negotiation'),
        ('NIH Stroke Scale Patient Assessment', 'NIH Stroke Scale Patient Assessment'),
        ('Objective-C', 'Objective-C'),
        ('Office Equipment', 'Office Equipment'),
        ('Open Source Experience', 'Open Source Experience'),
        ('Organization', 'Organization'),
        ('Pascal', 'Pascal'),
        ('Patient Assessment', 'Patient Assessment'),
        ('Patient Care', 'Patient Care'),
        ('Patient Education', 'Patient Education'),
        ('Performance Tracking', 'Performance Tracking'),
        ('Phlebotomy', 'Phlebotomy'),
        ('Photography and Branding', 'Photography and Branding'),
        ('PHP', 'PHP'),
        ('POS Skills', 'POS Skills'),
        ('PowerShell', 'PowerShell'),
        ('PPC', 'PPC'),
        ('Print Design', 'Print Design'),
        ('Problem Solving', 'Problem Solving'),
        ('Product Knowledge', 'Product Knowledge'),
        ('Profit and Loss', 'Profit and Loss'),
        ('Project Launch', 'Project Launch'),
        ('Project Lifecycle Management', 'Project Lifecycle Management'),
        ('Prolog', 'Prolog'),
        ('Prototyping', 'Prototyping'),
        ('Public relations', 'Public relations'),
        ('Public Speaking', 'Public Speaking'),
        ('Python', 'Python'),
        ('QuickBooks', 'QuickBooks'),
        ('R', 'R'),
        ('Rebol', 'Rebol'),
        ('Recording Patient Medical History', 'Recording Patient Medical History'),
        ('Record-Keeping', 'Record-Keeping'),
        ('Reducing Customer Acquisition Cost (CAC)', 'Reducing Customer Acquisition Cost (CAC)'),
        ('Referral Marketing', 'Referral Marketing'),
        ('Rehabilitation Therapy', 'Rehabilitation Therapy'),
        ('Ruby', 'Ruby'),
        ('Rust', 'Rust'),
        ('Sales Funnel Management', 'Sales Funnel Management'),
        ('Salesforce', 'Salesforce'),
        ('Scala', 'Scala'),
        ('Scheduling', 'Scheduling'),
        ('Scope Management', 'Scope Management'),
        ('Scratch', 'Scratch'),
        ('Scrum', 'Scrum'),
        ('Security', 'Security'),
        ('Self Motivation', 'Self Motivation'),
        ('SEO/SEM', 'SEO/SEM'),
        ('Shipping', 'Shipping'),
        ('Simula', 'Simula'),
        ('Smalltalk', 'Smalltalk'),
        ('Social Media Marketing and Paid Social Media Advertising',
         'Social Media Marketing and Paid Social Media Advertising'),
        ('SolidWorks', 'SolidWorks'),
        ('Speakeasy', 'Speakeasy'),
        ('SQL', 'SQL'),
        ('STEM Skills', 'STEM Skills'),
        ('Swift', 'Swift'),
        ('Taking Vital Signs', 'Taking Vital Signs'),
        ('Teamwork', 'Teamwork'),
        ('Technical Report Writing', 'Technical Report Writing'),
        ('Testing', 'Testing'),
        ('Troubleshooting', 'Troubleshooting'),
        ('TypeScript', 'TypeScript'),
        ('Typography', 'Typography'),
        ('Urgent and Emergency Care', 'Urgent and Emergency Care'),
        ('Use of X-Ray, MRI, CAT Scans', 'Use of X-Ray, MRI, CAT Scans'),
        ('UX/UI', 'UX/UI'),
        ('VBA', 'VBA'),
        ('Visual Basic', 'Visual Basic'),
        ('Web Development', 'Web Development'),
        ('Welcoming Visitors', 'Welcoming Visitors'),
        ('Workflow Development', 'Workflow Development'),
        ('Wound Dressing and Care', 'Wound Dressing and Care'),
        ('Marketing', 'Marketing'),
        ('Field Sales', 'Field Sales'),
        ('Sales', 'Sales'),
    ]
    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ]
    gender = models.CharField(blank=True,default='',choices=GENDER,max_length=20)
    dob = models.CharField(blank=True, max_length=140)
    mailid = models.CharField(blank=True, max_length=140)
    skill_info = MultiSelectField(blank=True,default='',choices=SKILLS,max_length=540)
    profile_pic = models.ImageField(default='avatar.jpg',null = True, blank = True)
    profile_resume = models.FileField(upload_to='resumes/',default='blank_resume.docx',null = True, blank = True)
    job_for_which_shortlisted=models.CharField(blank=True,default='',max_length=20)

    def _str_(self):
        return self.name

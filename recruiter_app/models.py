from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.urls import reverse
from datetime import datetime
from multiselectfield import MultiSelectField
from Profcess_Dev.settings import AUTH_USER_MODEL
User = AUTH_USER_MODEL
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
#from accounts.models import ProfcessUser
from applicant_app.models import ApplicantUserProfile
#User = ProfcessUser
can=ApplicantUserProfile



class RecruiterUserProfile(models.Model):
    first_name = models.CharField(blank=True, max_length=140)
    last_name = models.CharField(blank=True, max_length=140)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={"usertype": "Recruiter"},
        related_name="recruiteruserprofile"
    )
    COUNTRY_CHOICE = [
        ('India','India'),
        ('US','US'),
        ('Australia','Australia'),
        ('Mexico','Mexico'),
        ('UK','UK'),
        ('Italy','Italy'),
        ('Japan','Japan'),
        ('China', 'China'),
        ('France','France'),
        ('Germany','Germany'),
        ('Sri Lanka','Sri Lanka')
    ]
    STATE_CHOICES = [
        ('Andhra Pradesh (AP)', 'Andhra Pradesh (AP)'),
        ('Arunachal Pradesh (AR)', 'Arunachal Pradesh (AR)'),
        ('Assam (AS)', 'Assam (AS)'),
        ('Bihar (BR)', 'Bihar (BR)'),
        ('Chhattisgarh (CG)', 'Chhattisgarh (CG)'),
        ('Goa (GA)', 'Goa (GA)'),
        ('Gujarat (GJ)', 'Gujarat (GJ)'),
        ('Haryana (HR)', 'Haryana (HR)'),
        ('Himachal Pradesh (HP)', 'Himachal Pradesh (HP)'),
        ('Jammu and Kashmir (JK)', 'Jammu and Kashmir (JK)'),
        ('Jharkhand (JH)', 'Jharkhand (JH)'),
        ('Karnataka (KA)', 'Karnataka (KA)'),
        ('Kerala (KL)', 'Kerala (KL)'),
        ('Madhya Pradesh (MP)', 'Madhya Pradesh (MP)'),
        ('Maharashtra (MH)', 'Maharashtra (MH)'),
        ('Manipur (MN)', 'Manipur (MN)'),
        ('Meghalaya (ML)', 'Meghalaya (ML)'),
        ('Mizoram (MZ)', 'Mizoram (MZ)'),
        ('Nagaland (NL)', 'Nagaland (NL)'),
        ('Odisha(OR)', 'Odisha(OR)'),
        ('Punjab (PB)', 'Punjab (PB)'),
        ('Rajasthan (RJ)', 'Rajasthan (RJ)'),
        ('Sikkim (SK)', 'Sikkim (SK)'),
        ('Tamil Nadu (TN)', 'Tamil Nadu (TN)'),
        ('Telangana (TS)', 'Telangana (TS)'),
        ('Tripura (TR)', 'Tripura (TR)'),
        ('Uttar Pradesh (UP)', 'Uttar Pradesh (UP)'),
        ('Uttrakhand (UK)', 'Uttrakhand (UK)'),
        ('West Bengal (WB))', 'West Bengal (WB))')
    ]
    country = models.CharField(blank=True, max_length=140,choices=COUNTRY_CHOICE)
    state = models.CharField(blank=True, max_length=140,choices=STATE_CHOICES)
    #cell = models.CharField('Contact Phone', blank=True, max_length=10,
                               #validators=[MaxLengthValidator(10), MinLengthValidator(10)])
    #HR_email = models.EmailField('Email Address', blank=True)
    designation=models.CharField(default='',blank=True, max_length=140)
    company_name=models.CharField(default='',blank=True, max_length=140)
    Url_of_company=models.CharField(default='',blank=True, max_length=140)
    why_join_us=models.CharField(default='',blank=True, max_length=540)
    company_description=models.TextField(blank=True, max_length=540)
    profile_pic = models.ImageField(default='avatar.jpg',null = True, blank = True)
    username = models.CharField(default='',blank=True, max_length=140)
    email = models.EmailField(default='',blank=True, max_length=140)
    phone = PhoneNumberField(region="IN",default="")
    company_email = models.EmailField(default='',blank=True, max_length=140)
    location = models.CharField(default='',blank=True, max_length=140)

    def __str__(self):
        return self.name
    pass
#class State(models.Model):
 #   s_name = models.CharField('State Name', blank=True, max_length=140)
#
 #   def __str__(self):
  #      return self.s_name


#class City(models.Model):
 #   c_name = models.CharField('City Name', blank=True, max_length=140)
  #  state = models.ForeignKey(State, on_delete=models.CASCADE)

   # def __str__(self):
    #    return self.c_name


class Job(models.Model):
    job_title = models.CharField(blank=False, max_length=140)
    posted_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={"usertype": "Recruiter"},
        related_name="jobs",
        default="def",
        blank=True)
    applied_by = models.ManyToManyField(
        User,
        related_name="applied_by",
        limit_choices_to={"usertype": "Applicant"},
        blank=True)
    company_name = models.CharField('company name', max_length=30, blank=True)
    job_salary = models.PositiveIntegerField('Total CTC', blank=True, max_length=140, null=True)
    minimum = models.CharField('Minimum', blank=True, max_length=140, null=True)
    maximum = models.CharField('Maximum', blank=True, max_length=140, null=True)
    TYPE_OF_JOB_CHOICES = [
        ('Full Time', 'FULL TIME'),
        ('contract', 'CONTRACT'),
        ('part time', 'PART TIME'),
        ('internship', 'INTERNSHIP'),
        ('volunteer', 'VOLUNTEER'),
        ('temporary', 'TEMPORARY'),
        ('remote', 'REMOTE'),
    ]
    PRIMARY_PROFILE_CHOICES = [
        ('Business Development', 'Business Development'),
        ('Graphic Design', 'Graphic Design'),
        ('Social Media Marketing', 'Social Media Marketing'),
        ('Web Development', 'Web Development'),
        ('Content Writing', 'Content Writing'),
        ('Marketing', 'Marketing'),
        ('Operations', 'Operations'),
        ('App Development', 'App Development'),
        ('Human Resource(HR)', 'Human Resource(HR)'),
        ('Public Relations', 'Public Relations'),
        ('Digital Marketing', 'Digital Marketing'),
        ('Research & Development', 'Research & Development'),
        ('Creative Designing', 'Creative Designing'),
        ('Law Legal', 'Law Legal'),
        ('Design', 'Design'),
        ('Software Development','Software Development'),
        ('Others', 'Others'),
    ]

    primary_profile = models.CharField('Primary Profile',
                                       max_length=50,
                                       choices=PRIMARY_PROFILE_CHOICES,
                                       default="",
                                       blank=False
                                       )

    # type_of_job = models.CharField('TYPE OF JOB',
    #                              max_length=35,
    #                             choices=TYPE_OF_JOB_CHOICES,
    #                            default=""
    #                           )
    JOB_LOCATION_CHOICES = [
        ('Work From Home', 'Work From Home'),
        ('ahemdabad', 'Ahmedabad'),
        ('bengaluru', 'Bengaluru'),
        ('chennai', 'Chennai'),
        ('delhi', 'Delhi'),
        ('hydradad', 'Hyderabad'),
        ('jaipur', 'Jaipur'),
        ('kolkata', 'Kolkata'),
        ('mumbai', 'Mumbai'),
        ('pune', 'Pune'),
        ('surat', 'Surat'),
        ('vishakhapatnam', 'Vishakhapatnam')
    ]
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
    STATE_CHOICES = [
        ('Andhra Pradesh (AP)', 'Andhra Pradesh (AP)'),
        ('Arunachal Pradesh (AR)', 'Arunachal Pradesh (AR)'),
        ('Assam (AS)', 'Assam (AS)'),
        ('Bihar (BR)', 'Bihar (BR)'),
        ('Chhattisgarh (CG)', 'Chhattisgarh (CG)'),
        ('Goa (GA)', 'Goa (GA)'),
        ('Gujarat (GJ)', 'Gujarat (GJ)'),
        ('Haryana (HR)', 'Haryana (HR)'),
        ('Himachal Pradesh (HP)', 'Himachal Pradesh (HP)'),
        ('Jammu and Kashmir (JK)', 'Jammu and Kashmir (JK)'),
        ('Jharkhand (JH)', 'Jharkhand (JH)'),
        ('Karnataka (KA)', 'Karnataka (KA)'),
        ('Kerala (KL)', 'Kerala (KL)'),
        ('Madhya Pradesh (MP)', 'Madhya Pradesh (MP)'),
        ('Maharashtra (MH)', 'Maharashtra (MH)'),
        ('Manipur (MN)', 'Manipur (MN)'),
        ('Meghalaya (ML)', 'Meghalaya (ML)'),
        ('Mizoram (MZ)', 'Mizoram (MZ)'),
        ('Nagaland (NL)', 'Nagaland (NL)'),
        ('Odisha(OR)', 'Odisha(OR)'),
        ('Punjab (PB)', 'Punjab (PB)'),
        ('Rajasthan (RJ)', 'Rajasthan (RJ)'),
        ('Sikkim (SK)', 'Sikkim (SK)'),
        ('Tamil Nadu (TN)', 'Tamil Nadu (TN)'),
        ('Telangana (TS)', 'Telangana (TS)'),
        ('Tripura (TR)', 'Tripura (TR)'),
        ('Uttar Pradesh (UP)', 'Uttar Pradesh (UP)'),
        ('Uttrakhand (UK)', 'Uttrakhand (UK)'),
        ('West Bengal (WB))', 'West Bengal (WB))')
    ]
    CITY_CHOICES = [
        ('Agra', 'Agra'),
        ('Ahmedabad', 'Ahmedabad'),
        ('Ajmer', 'Ajmer'),
        ('Aligarh', 'Aligarh'),
        ('Allahabad', 'Allahabad'),
        ('Ambala', 'Ambala'),
        ('Amritsar', 'Amritsar'),
        ('Bangalore', 'Bangalore'),
        ('Bareilly', 'Bareilly'),
        ('Bharatpur', 'Bharatpur'),
        ('Bhilwara', 'Bhilwara'),
        ('Bhojpur', 'Bhojpur'),
        ('Bhopal', 'Bhopal'),
        ('Chandigarh', 'Chandigarh'),
        ('Chennai', 'Chennai'),
        ('Chhatarpur', 'Chhatarpur'),
        ('Chitrakoot', 'Chitrakoot'),
        ('Churu', 'Churu'),
        ('Coimbatore', 'Coimbatore'),
        ('Daman', 'Daman'),
        ('Darbhanga', 'Darbhanga'),
        ('Darjeeling', 'Darjeeling'),
        ('Dehradun', 'Dehradun'),
        ('Dholpur', 'Dholpur'),
        ('Diu', 'Diu'),
        ('Delhi', 'Delhi'),
        ('Sikkim', 'Sikkim'),
        ('Faridabad', 'Faridabad'),
        ('Fatehabad', 'Fatehabad'),
        ('Fatehpur', 'Fatehpur'),
        ('Firozabad', 'Firozabad'),
        ('Gandhinagar', 'Gandhinagar'),
        ('Ganganagar', 'Ganganagar'),
        ('Garhwa', 'Garhwa'),
        ('Gaya', 'Gaya'),
        ('Gautam Buddh Nagar', 'Gautam Buddh Nagar'),
        ('Ghaziabad', 'Ghaziabad'),
        ('Ghazipur', 'Ghazipur'),
        ('Gurgaon', 'Gurgaon'),
        ('Gwalior', 'Gwalior'),
        ('Hamirpur', 'Hamirpur'),
        ('Haridwar', 'Haridwar'),
        ('Hissar', 'Hissar'),
        ('Hooghly', 'Hooghly'),
        ('Hyderabad', 'Hyderabad'),
        ('Indore', 'Indore'),
        ('Jaipur', 'Jaipur'),
        ('Jaisalmer', 'Jaisalmer'),
        ('Jalandhar', 'Jalandhar'),
        ('Jammu', 'Jammu'),
        ('Jhansi', 'Jhansi'),
        ('Jodhpur', 'Jodhpur'),
        ('Kanchipuram', 'Kanchipuram'),
        ('Kanpur', 'Kanpur'),
        ('Kanyakumari', 'Kanyakumari'),
        ('Kargil ', 'Kargil'),
        ('Kohima', 'Kohima'),
        ('Kolhapur', 'Kolhapur'),
        ('Kolkata', 'Kolkata'),
        ('Kota', 'Kota'),
        ('Kottayam', 'Kottayam'),
        ('Kozhikode', 'Kozhikode'),
        ('Kurnool', 'Kurnool'),
        ('Kurukshetra', 'Kurukshetra'),
        ('Kutch', 'Kutch'),
        ('Lalitpur', 'Lalitpur'),
        ('Leh', 'Leh'),
        ('Lucknow', 'Lucknow'),
        ('Ludhiana', 'Ludhiana'),
        ('Madurai', 'Madurai'),
        ('Mainpuri', 'Mainpuri'),
        ('Mathura', 'Mathura'),
        ('Meerut', 'Meerut'),
        ('Mumbai ', 'Mumbai'),
        ('Muzaffarnagar', 'Muzaffarnagar'),
        ('Mysore', 'Mysore'),
        ('Nagpur', 'Nagpur'),
        ('Nainital', 'Nainital'),
        ('Nashik ', 'Nashik'),
        ('Nanital', 'Nanital'),
        ('Pali', 'Pali'),
        ('Panipat', 'Panipat'),
        ('Patna', 'Patna'),
        ('Pithoragarh', 'Pithoragarh'),
        ('Pondicherry', 'Pondicherry'),
        ('Pune', 'Pune'),
        ('Raigarh', 'Raigarh'),
        ('Raipur', 'Raipur'),
        ('Rajkot', 'Rajkot'),
        ('Ramgarh ', 'Ramgarh'),
        ('Ranchi', 'Ranchi'),
        ('Rohta', 'Rohta'),
        ('Sambalpur', 'Sambalpur'),
        ('Shimla', 'Shimla'),
        ('Sikar', 'Sikar'),
        ('Solapur', 'Solapur'),
        ('Sonipat', 'Sonipat'),
        ('Srinagar', 'Srinagar'),
        ('Surat', 'Surat'),
        ('Thane', 'Thane'),
        ('Thrissur', 'Thrissur'),
        ('Tiruchirappalli', 'Tiruchirappalli'),
        ('Tonk', 'Tonk'),
        ('Thiruvananthapuram', 'Thiruvananthapuram'),
        ('Udaipur', 'Udaipur'),
        ('Udupi', 'Udupi'),
        ('Ujjain', 'Ujjain'),
        ('Uttarkashi', 'Uttarkashi'),
        ('Vadodara', 'Vadodara'),
        ('Varanasi', 'Varanasi'),
        ('Vellore', 'Vellore'),
        ('Visakhapatnam', 'Visakhapatnam'),
    ]
    # JOB_DURATION_CHOICES = [
    #   ('1 year', '1 year'),
    #  ('2 year', '2 year'),
    # ('3 year', '3 year')]
    WORKING_HOUR_CHOICES = [
        ('Eight Hour', 'Eight Hour'),
        ('Ten Hour', 'Ten Hour'),
        ('Twelve Hour', 'Twelve Hour')]

    EDUCATION_QUALI = [
        ('10th Class', '10th Class'),
        ('12th Class', '12th Class'),
        ('Diploma', 'Diploma'),
        ('Graduate', 'Graduate'),
        ('Post Graduate', 'Post Graduate'),
    ]
    EXP_REQ = [
        ('0 ', '0 '),
        ('0-1 year', '0-1 year'),
        ('1-2 years', '1-2 years'),
        ('2-3 years', '2-3 years'),
        ('3-5 years', '3-5 years'),
        ('5-10 years', '5-10 years'),
        ('10+ years', '10+ years')]

    PERK_CHOICES = [
        ('Certification', 'Certification'),
        ('Letter of Recommendation', 'Letter of Recommendation'),
        ('Flexible Work Hours', 'Flexible Work Hours'),
        ('Five Days a Week', 'Five Days a Week'),
        ('Other', 'Other')
    ]
    NOTICE_CHOICES = [
        ('Immediate Joiner', 'Immediate Joiner'),
        ('1 Month', '1 Month'),
        ('2 Month', '2 Month'),
        ('3 Month', '3 Month'),
        ('3 Month+', '3 Month+'),
    ]

    INDUSTRY_TYPE_CHOICES = [
        ('Textile Industry', 'Textile Industry'),
        ('Food Processing Industry', 'Food Processing Industry'),
        ('Chemical Industry', 'Chemical Industry'),
        ('Steel Industry', 'Steel Industry'),
        ('Cement Industry', 'Cement Industry'),
        ('Mining Industry', 'Mining Industry'),
        ('Petroleum Industry', 'Petroleum Industry'),
        ('IT/Computers-Hardware', 'IT/Computers-Hardware'),
        ('IT/Computers-Software', 'IT/Computers-Software'),
        ('Media And Entertainment', 'Media And Entertainment'),
        ('Telecommunications', 'Telecommunications'),
        ('Retail', 'Retail'),
        ('Consumer Products', 'Consumer Products'),
        ('Manufacturing', 'Manufacturing'),
        ('Technology', 'Technology'),

    ]
    VACANCY_CHOICES = [
        ('1', '1'),
        ('2-3', '2-3'),
        ('4-5', '4-5'),
        ('5-10', '5-10'),
        ('10+', '10+'),

    ]


    job_vacancies = models.CharField('Number of Openings',
                                     max_length=80,
                                     choices=VACANCY_CHOICES,
                                     default="",
                                     blank=False
                                     )
    immediately = models.BooleanField('immediately', default="")

    perks = models.CharField('Perks',
                             max_length=80,
                             choices=PERK_CHOICES,
                             default=""
                             )
    working_hour = models.CharField('Working Hour',
                                    choices=WORKING_HOUR_CHOICES,
                                    max_length=80,
                                    default=""
                                    )
    job_city = models.CharField('City',
                               choices=CITY_CHOICES,
                              max_length=100,
                             default="",
                            blank=False
                           )

    # job_duration = models.CharField('Job Duration',
    #                               max_length=80,
    #                              default=""
    #                             )

    exp_req = models.CharField('Experience Required',
                               max_length=80,
                               choices=EXP_REQ,
                               blank=False,
                               default="")
    state = models.CharField('State',
                            max_length=80,
                           choices=STATE_CHOICES,
                          default="",
                         blank=True
                        )
    job_location = models.CharField('JOB LOCATION',
                                    max_length=35,
                                    choices=JOB_LOCATION_CHOICES,
                                    default=""
                                    )
    job_requirements = MultiSelectField('Skills Required*',
                                        choices=SKILLS,
                                        max_length=200,
                                        blank=True
                                        )
    education_quali = MultiSelectField('Education Qualification*',
                                       choices=EDUCATION_QUALI,
                                       max_length=540,
                                       default="",
                                       blank=True
                                       )
    job_info = models.TextField('Job Description', blank=False,
                                max_length=1000)

    types_of_job = models.CharField('types of job', max_length=250, default="",
                                    choices=[('Part Time', 'Part Time'),
                                             ('Full Time', 'Full Time'),
                                             ('Work from home', 'Work from home'),
                                             ('Internship', 'Internship')
                                             ])
    notice_period = models.CharField('NOTICE PERIOD',
                                     max_length=35,
                                     choices=NOTICE_CHOICES,
                                     default=""
                                     )
    industry_type = models.CharField('Industry Type',
                                     max_length=100,
                                     choices=INDUSTRY_TYPE_CHOICES,
                                     default=""
                                     )
    start_date = models.CharField('Start Date', blank=True, max_length=140)
    pincode = models.CharField('Location Pincode', null=True, blank=True, max_length=100)
    functional_area = models.TextField('Functional Area', max_length=100, default="")
    job_role = models.TextField('Job Role', max_length=100, default="")
    responsibility = models.TextField('Responsibility', max_length=100, default="")

    #essential_skills = models.CharField('Essential Skills', max_length=100, default="", blank=False)
    cert = models.BooleanField('cert', default="")
    lor = models.BooleanField('lor', default="")
    wh = models.BooleanField('wh', default="")
    others = models.BooleanField('others', default="")

    cert_req = models.CharField('Certification Required', max_length=100, default="", blank=True)
    other = models.CharField('Other', max_length=100, default="", blank=True)

    # job_starting_date = models.DateTimeField(
    #     verbose_name=_('Date joined'), auto_now_add=True)
    #state = models.ForeignKey(State, on_delete=models.SET_NULL, blank=True, null=True)
    #city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.job_title

    pass

    def get_absolute_url(self):  # redirect to job details after updation
        return reverse('recruiter:job_detail', kwargs={'pk': self.pk})


class UserData(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={"usertype": "Recruiter"},
    )
    token = models.IntegerField(null=True, blank=True,default=10)

    def str(self):
        return self.user.username

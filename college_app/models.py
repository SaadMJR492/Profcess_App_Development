from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.urls import reverse
from multiselectfield import MultiSelectField

# Create your models here.
from accounts.models import ProfcessUser
User = ProfcessUser
class CollegeUserProfile(models.Model):
    name = models.CharField(blank=True, max_length=140)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={"usertype": "College"},
        related_name="collegeuserprofile"
    )
    location = models.CharField(blank=True, max_length=140)
    #cell = models.CharField('Contact Phone', blank=True, max_length=10,
                               #validators=[MaxLengthValidator(10), MinLengthValidator(10)])
    #HR_email = models.EmailField('Email Address', blank=True)
    designation=models.CharField(default='',blank=True, max_length=140)
    college_name=models.CharField(default='',blank=True, max_length=140)
    url_of_college=models.CharField(default='',blank=True, max_length=140)
    why_join_us=models.CharField(default='',blank=True, max_length=540)
    college_description=models.CharField(blank=True, max_length=540)

    def __str__(self):
        return self.name
    pass
class Jobs(models.Model):
    job_title = models.CharField(blank=True, max_length=140)
    posted_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={"usertype": "College"},
        related_name="college_jobs",
        default="def",
        blank=True)
    applied_by = models.ManyToManyField(
        User,
        related_name="applied_by_students",
        limit_choices_to={"usertype": "Applicant"},
        blank=True)

    company_name = models.CharField('company name', max_length=30, blank=True)
    job_salary = models.PositiveIntegerField('Total CTC', blank=True, max_length=140, null=True)
    minimum = models.PositiveIntegerField('Minimum', blank=True, max_length=140, null=True)
    maximum = models.PositiveIntegerField('Maximum', blank=True, max_length=140, null=True)
    job_vacancies = models.PositiveIntegerField('Number of Openings', default=1, blank=True)


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
        ('Others', 'Others'),
    ]

    primary_profile = models.CharField('Primary Profile',
                                       max_length=50,
                                       choices=PRIMARY_PROFILE_CHOICES,
                                       default=""
                                       )

    #type_of_job = models.CharField('TYPE OF JOB',
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
        ('CRM Software (Salesforce, Hubspot, Zoho, Freshsales)', 'CRM Software (Salesforce, Hubspot, Zoho, Freshsales)'),
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
        ('Marketing','Marketing'),
        ('Field Sales','Field Sales'),
        ('Sales','Sales'),
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

    WORKING_HOUR_CHOICES = [
        ('Eight Hour', 'Eight Hour'),
        ('Ten Hour', 'Ten Hour'),
        ('Twelve Hour', 'Twelve Hour')]

    EDUCATION_QUALI = [
        ('10th Class', '10th Class'),
        ('12th Class', '12th Class'),
        ('Diploma', 'Diploma'),
        ('Graduate','Graduate'),
        ('Post Graduate','Post Graduate'),
    ]
    EXP_REQ = [
        ('0 year(Freshers may apply)','0 year(Freshers may apply)'),
        ('1 year', '1 year'),
        ('2 year', '2 year'),
        ('3 year', '3 year')]

    PERK_CHOICES = [
        ('Certification','Certification'),
        ('Letter of Recommendation','Letter of Recommendation'),
        ('Flexible Work Hours','Flexible Work Hours'),
        ('Five Days a Week','Five Days a Week'),
        ('Other','Other')
    ]
    NOTICE_CHOICES = [
        ('One Month', 'One Month'),
        ('Two Month', 'Two Month'),
        ('Three Month', 'Three Month'),
        ('Four Month', 'Four Month'),
        ('Five Month', 'Five Month'),
        ('Six Month', 'Six Month')
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
        ('One Candidate', 'One Candidate'),
        ('Two Candidate', 'Two Candidate'),
        ('Three Candidate', 'Three Candidate'),
        ('Four Candidate', 'Four Candidate'),
        ('Five Candidate', 'Five Candidate'),
        ('Six Candidate', 'Six Candidate')
    ]
    EXP_REQ = [
        ('0 year(Freshers may apply)', '0 year(Freshers may apply)'),
        ('1 year', '1 year'),
        ('2 year', '2 year'),
        ('3 year', '3 year')]
    JOB_DURATION_CHOICES = [
        ('1 year', '1 year'),
        ('2 year', '2 year'),
        ('3 year', '3 year')]


    job_vacancies = models.CharField('Number of Openings',
                                     max_length=80,
                                     choices=VACANCY_CHOICES,
                                     default=""
                                     )

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
    city = models.CharField('City',
                                choices=CITY_CHOICES,
                                max_length=100,
                                default=""
                                )

    #job_duration = models.CharField('Job Duration',
     #                               max_length=80,
      #                              default=""
       #                             )

    exp_req = models.CharField('Experience Required',
                               max_length=80,
                               choices=EXP_REQ,

                               default="")
    state = models.CharField('State',
                             max_length=80,
                             choices=STATE_CHOICES,
                             default=""
                             )
    job_location = models.CharField('JOB LOCATION',
                                    max_length=35,
                                    choices=JOB_LOCATION_CHOICES,
                                    default=""
                                    )
    job_requirements = MultiSelectField('Skills Required',
                                        choices=SKILLS,
                                        max_length=200
                                        )
    education_quali = MultiSelectField('Education Qualification',
                                       choices=EDUCATION_QUALI,
                                       max_length=540,
                                       default="",
                                       )
    job_info = models.TextField('Job Description', blank=True,
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
    job_duration = models.CharField('Job Duration',
                                    max_length=80,
                                    default=""
                                    )
    start_date = models.CharField('Start Date', blank=True, max_length=140)
    pincode = models.CharField('Location Pincode', null=True, blank=True, max_length=100)
    functional_area = models.TextField('Functional Area', max_length=100, default="")
    job_role = models.TextField('Job Role', max_length=100, default="")
    responsibility = models.TextField('Responsibility', max_length=100, default="")

    essential_skills = models.CharField('Essential Skills', max_length=100, default="")
    cert = models.BooleanField('cert', default="True")
    lor = models.BooleanField('lor', default="True")
    wh = models.BooleanField('wh', default="True")
    others = models.BooleanField('others', default="True")

    cert_req = models.CharField('Certification Required', max_length=100, default="")
    other = models.CharField('Other', max_length=100, default="")
    def __str__(self):
        return self.job_title

    pass

    def get_absolute_url(self):  # redirect to job details after updation
        return reverse('college:job_detail', kwargs={'pk': self.pk})


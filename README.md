# Profcess_Dev

This the Profcess Website (development) repo.

1. **Instructions to setup DATABASES in settings.py after cloning Ananya_Mitra branch.
(Important : Please undo the database edits before pushing to this branch)**

    b. Comment the currect default database as shown below.

        If you have sqlite installed on your machine, apply the following:

        `DATABASES = {
          'default': {
              'ENGINE': 'django.db.backends.sqlite3',
              'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }`

    a. Replace database as per your choice:

    1. If you have mysql installed on your machine, apply the following:

        DATABASES = {
        'default': {

            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'UATprofcess$profcess',
            'USER': 'UATprofcess',
            'PASSWORD': 'Horizon@13',
            'HOST': 'UATprofcess.mysql.pythonanywhere-services.com',
            'PORT': '3306',
            }
        }        
    2. If you have mysql and xampp server installed :
    
        `DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '<your_database_name>',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
            }
        }`

2. **Instructions to setup ALLOWED_HOSTS in settings.py after cloning Ananya_Mitra branch.
(Important : Please undo the ALLOWED_HOSTS edit before pushing to this branch)**


        Current status :
        ALLOWED_HOSTS = []


        Replace it with :
        ALLOWED_HOSTS = ['UATProfcess.pythonanywhere.com']


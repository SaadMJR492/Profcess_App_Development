from django.contrib.sites.models import Site
sites=Site()
sites.domain='http://uatprofcess.pythonanywhere.com/'
sites.name='http://uatprofcess.pythonanywhere.com/'
sites.save()
#global S_ID
S_ID=sites.id
print(S_ID)

#exec(open('site_id_script.py').read())

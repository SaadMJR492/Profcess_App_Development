from django.contrib.sites.models import Site
sites=Site()
sites.domain='https://guarded-spire-91535.herokuapp.com/'
sites.name='https://guarded-spire-91535.herokuapp.com/'
sites.save()
#global S_ID
S_ID=sites.id
print(S_ID)

#exec(open('site_id_script.py').read())

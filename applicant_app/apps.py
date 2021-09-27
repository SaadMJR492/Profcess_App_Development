from __future__ import unicode_literals
from django.apps import AppConfig


class ApplicantAppConfig(AppConfig):
    name = 'applicant_app'
    def ready(self):
       import applicant_app.signals


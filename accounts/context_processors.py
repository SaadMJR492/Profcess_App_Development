from django.conf import settings
from django.shortcuts import render, redirect
from .forms import CFormFooter
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.contrib import messages

def Fcontact(request):
    if request.method == 'POST':
        Cform=CFormFooter(request.POST)
        if Cform.is_valid():
            sender_name=Cform.cleaned_data.get('uname')
            from_mail=Cform.cleaned_data.get('mail')
            tel_phone=Cform.cleaned_data.get('telephone')
            mail_info=Cform.cleaned_data.get('message')
            subject="Website Contact Form: "+sender_name
            mail_body="You have received a new message from your website contact form.\n\nHere are the details:\n\nName: "+str(sender_name)+"\n\nEmail: "+str(from_mail)+"\n\nPhone: "+str(tel_phone)+"\n\nMessage:\n"+str(mail_info)
            send_mail(subject,mail_body,from_mail,['contact@profcess.com'],fail_silently=True)
            messages.info(request,"Your message has been sent successfully!")
        pass
    else:
        Cform = CFormFooter()
    context = {
            'Cform': Cform,
        }
    return context
    pass
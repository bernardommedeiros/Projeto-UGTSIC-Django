from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail as django_send_mail

def send_email(request):
    if request.method == 'POST':
        django_send_mail(
            subject='Subject here',
            message='Here is the message.',
            from_email='bernardo.moura@escolar.ifrn.edu.br',
            recipient_list=['bernardo181105@gmail.com'],
            fail_silently=False,
        )
        return HttpResponse("Mail sent!")
    return render(request, 'cv_hub/send_mail.html')
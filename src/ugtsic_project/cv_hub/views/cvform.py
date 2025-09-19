from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models.cv import CV
from ..services import cvform as service
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

class CVCreateView(LoginRequiredMixin, View):
    def get(self, request):
        ip_address = request.META.get('REMOTE_ADDR')
        return render(request, 'cv_hub/create_cv.html', {'ip_address': ip_address})

    def post(self, request):
        ip_address = request.META.get('REMOTE_ADDR')
        data = request.POST.copy()
        data['ip_address'] = ip_address
        files = request.FILES

        cv = service.create_cv(request.user, data, files)

        message_html = render_to_string('cv_hub/email.txt', {'cv': cv})

        email = EmailMessage(
            subject='UGTSIC CV HUB - Nova inscrição',
            message=message_html,
            from_email='bernardo.moura@escolar.ifrn.edu.br',
            recipient_list=['bernardo181105@gmail.com'],
            fail_silently=False,
        )

        if cv.cv_file:
            email.attach(cv.cv_file.name, cv.cv_file.read(), cv.cv_file.content_type)
        email.send(fail_silently=False)

        return redirect('home_page')

class CVUpdateView(LoginRequiredMixin, View):
    def get(self, request):
        cv = CV.objects.filter(user=request.user).first()
        if not cv:
            return redirect('create_cv')
        return render(request, 'cv_hub/update_cv.html', {'cv': cv})

    def post(self, request):
        cv = CV.objects.filter(user=request.user).first()
        if not cv:
            return redirect('create_cv')
        data = request.POST
        files = request.FILES
        service.update_cv(cv, data, files)

        message_html = render_to_string('cv_hub/email.txt', {'cv': cv})
        email = EmailMessage(
            subject='Currículo Atualizado',
            body=message_html,
            from_email='bernardo.moura@escolar.ifrn.edu.br',
            to=['bernardo181105@gmail.com'],
        )

        if cv.cv_file:
            email.attach_file(cv.cv_file.path)

        email.send(fail_silently=False)
        
        return redirect('home_page')
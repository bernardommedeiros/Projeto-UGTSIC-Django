from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models.cv import CV
from ..services import cvform as service

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
        return redirect('home_page')
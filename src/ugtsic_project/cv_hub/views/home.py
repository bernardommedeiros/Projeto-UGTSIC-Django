from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models.cv import CV
from ..services.home import show_cv, get_all_cvs

class HomePageView(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.is_superuser:
            cvs = get_all_cvs()  # superuser 
            cv = None
        else:
            cv = show_cv(request.user) 
            cvs = None

        return render(request, 'cv_hub/home_page.html', {
            'cv': cv,
            'cvs': cvs
        })
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models.cv import CV
from ..services.home import show_cv

class HomePageView(LoginRequiredMixin, View):
    def get(self, request):
        cv = show_cv(request.user)
        return render(request, 'cv_hub/home_page.html', {'cv': cv})
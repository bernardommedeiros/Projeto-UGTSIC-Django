from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from ..services import home as service
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models.cv import CV

class HomePageView(LoginRequiredMixin, View):
    def get(self, request):
        cv = service.show_cv()
        return render(request, 'cv_hub/home_page.html', {'cv': cv})
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'intro/homepage.html'


class ProtectedView(LoginRequiredMixin, TemplateView):
    template_name = 'intro/protected.html'


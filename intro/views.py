from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, TemplateView, UpdateView

from intro.forms import CommentForm
from intro.models import Comment, ContactMessage


class HomeView(TemplateView):
    template_name = 'intro/homepage.html'


class ProtectedView(LoginRequiredMixin, TemplateView):
    template_name = 'intro/protected.html'


class CommentCreateView(CreateView):
    model = Comment
    template_name = 'intro/comment_edit.html'
    success_url = '/'
    fields = ['person', 'text']


class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'templates/intro/comment_edit.html'
    success_url = '/thank-you/'


class ContactMessageView(CreateView):
    model = ContactMessage
    fields = ['text', 'email']


class ContactMessageUpdateView(UpdateView):
    model = ContactMessage
    fields = ['text', 'email']
    success_url = '/thank-you/'

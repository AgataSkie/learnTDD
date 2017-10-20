import pytest

from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory

from mixer.backend.django import mixer

from intro import views

pytestmark = pytest.mark.django_db



class TestHomeView:
    def test_anonymous(self):
        req = RequestFactory().get('/')
        resp = views.HomeView.as_view()(req)  # !! Structure
        assert resp.status_code == 200, 'Homepage can be seen'


class TestLoginRequiredView:
    def test_anonymous(self):
        req = RequestFactory().get('/')
        req.user = AnonymousUser()
        req.session = {}
        resp = views.ProtectedView.as_view()(req)
        assert resp.status_code == 302, 'User should be redirected'
        assert '/login/' in resp.url, 'User should be redirected to login'

    def test_logged_in(self):
        req = RequestFactory().get('/')
        req.user = mixer.blend('auth.User')
        resp = views.ProtectedView.as_view()(req)
        assert resp.status_code == 200, 'Logged in user should see the page'

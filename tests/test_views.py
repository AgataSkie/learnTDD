from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory
from intro import views


class TestHomeView:
    def test_anonymous(self):
        req = RequestFactory().get('/')
        resp = views.HomeView.as_view()(req)  # !!
        assert resp.status_code == 200, 'Homepage can be seen'


class TestLoginRequiredView:
    def test_protected_page(self):
        req = RequestFactory().get('/')
        req.user = AnonymousUser()
        req.session = {}
        resp = views.ProtectedView.as_view()(req)  # !!
        assert resp.status_code == 302, 'User should be redirected'
        assert '/login/' in resp.url, 'User should be redirected to login'

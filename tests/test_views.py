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


class TestCommentView:

    def test_GET_comment_create_view(self):
        req = RequestFactory().get('/')
        resp = views.CommentCreateView.as_view()(req)
        assert resp.status_code == 200

    def test_GET_comment_update_view(self):
        req = RequestFactory().get('/')
        obj = mixer.blend('intro.Comment')
        resp = views.CommentCreateView.as_view()(req, pk=obj.pk)
        assert resp.status_code == 200

    def test_POST_comment_update_view(self):
        person = mixer.blend('intro.Person')
        comment = mixer.blend('intro.Comment')
        data = {'person': person.pk, 'text': 'Nothing important'}

        req = RequestFactory().post('/', data=data)
        resp = views.CommentUpdateView.as_view()(req, pk=comment.pk)
        assert resp.status_code == 302, 'Should redirect to thank-you'


class TestContactMessageView:

    def test_GET_contact_create_view(self):
        req = RequestFactory().get('/')
        resp = views.ContactMessageView.as_view()(req)
        assert resp.status_code == 200

    def test_GET_contact_update_view(self):
        obj = mixer.blend('intro.ContactMessage')
        req = RequestFactory().get('/')
        resp = views.ContactMessageUpdateView.as_view()(req, pk=obj.pk)
        assert resp.status_code == 200

    def test_POST_contact_update_view(self):
        obj = mixer.blend('intro.ContactMessage')
        data = {'text': 'Sample text...', 'email': 'someone@here.eu'}
        req = RequestFactory().post('/', data=data)
        resp = views.ContactMessageUpdateView.as_view()(req, pk=obj.pk)
        assert resp.status_code == 302, 'Should redirect to thank-you'
        obj.refresh_from_db()
        assert obj.text == data['text']
        assert obj.email == data['email']
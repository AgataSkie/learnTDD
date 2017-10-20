import pytest

from mixer.backend.django import mixer

from intro import forms

pytestmark = pytest.mark.django_db

class TestPostForm:
    def test_blank_form(self):
        form = forms.CommentForm(data={})
        assert form.is_valid() is False, 'required fields are blank, should be invalid'
        assert 'person' in form.errors

    def test_form_too_short_text(self):
        person = mixer.blend('intro.Person')
        form = forms.CommentForm(data={'person': person.pk, 'text': '.'})
        assert form.is_valid() is False, 'Text should be longer than 1 char'

    def test_correct_form(self):
        person = mixer.blend('intro.Person')
        form = forms.CommentForm(
            data={'person': person.pk, 'text': 'Some comment text'}
        )
        assert form.is_valid() is True, 'filled in form should be valid'

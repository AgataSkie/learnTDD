# Tutorial: The Django Test Driven Development Cookbook - Singapore Djangonauts
import pytest
from mixer.backend.django import mixer

from intro.views import get_short_desr

pytestmark = pytest.mark.django_db


class TestPerson:

    def test_descr(self):
        obj = mixer.blend('intro.Person')
        assert obj.description is not None, "Person object should be created"

    def test_get_short_desr(self):
        obj = mixer.blend('intro.Person', description='To jest tekscik testowy')
        short = get_short_desr(obj.description)
        assert len(short) == 10, 'Should return first 10 characters'
        assert short == 'To jest te', 'Should return first 10 characters'

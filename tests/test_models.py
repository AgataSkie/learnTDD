# Tutorial: The Django Test Driven Development Cookbook - Singapore Djangonauts
import pytest
from mixer.backend.django import mixer
# possible error: importing just mixer !

pytestmark = pytest.mark.django_db
# allow using db


class TestPerson:

    def test_descr(self):

        obj = mixer.blend('intro.Person')
        # arg: folder + model

        assert obj.description is not None, "Person object should be created"
        # second arg: message on fail

    def test_get_short_descr(self):
        obj = mixer.blend('intro.Person', description='To jest tekscik testowy')
        short = obj.get_short_descr(10)
        assert len(short) == 10, 'Should return first 10 characters'
        assert short == 'To jest te', 'Should return first 10 characters'

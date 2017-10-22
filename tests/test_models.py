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


class TestComment:

    # comment should have a relation to a person that the comment is about
    def test_comment_creation(self):
        person = mixer.blend('intro.Person')
        comment = mixer.blend('intro.Comment', person=person)
        assert comment.person is not None
        assert comment.text is not None


class TestContactMessage:

    def test_contact_message_creation(self):
        message = mixer.blend('intro.ContactMessage')
        assert message.text is not None
        assert message.email is not None

from django.db import models


class Person(models.Model):
    description = models.CharField(max_length=128)

    def get_short_descr(self, num):
        return self.description[:num]


class Comment(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    text = models.TextField()


class ContactMessage(models.Model):
    text = models.TextField()
    email = models.CharField(max_length=128)

from django.db import models


class Person(models.Model):
    description = models.CharField(max_length=128)

    def get_short_descr(self, num):
        return self.description[:num]
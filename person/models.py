from django.db import models

class Person(models.Model):

        lastname = models.CharField(max_length=100)
        middlename = models.CharField(max_length=100)
        firstname = models.CharField(max_length=100)
        degree = models.CharField(max_length=100)

        def __str__(self):
            return self.lastname

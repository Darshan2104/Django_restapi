from django.db import models

class Student(models.Model):
    name = models.CharField(max_length = 200)
    subject = models.CharField(max_length = 200)

    def __str__(self):
        return self.name
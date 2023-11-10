from django.db import models

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    birthdate = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.full_name} \t {self.birthdate}'
from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    phone=models.CharField(max_length=15)
    email=models.CharField(max_length=122)
    desc=models.TextField(max_length=122)
    date=models.DateField(auto_now_add=False)

    def __str__(self):
        return self.name
    
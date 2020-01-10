from django.db import models


# Create your models here.
class salon(models.Model):
    img = models.ImageField(upload_to='images')
    name = models.CharField(max_length=100)


class salon1(models.Model):
    img1 = models.ImageField(upload_to='images')
    name1 = models.CharField(max_length=100)


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class sal(models.Model):
    img=models.ImageField(upload_to='images')
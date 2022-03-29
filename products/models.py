from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    email = models.CharField(max_length=255)  # this has used to show title / heading
    pub_date = models.DateTimeField()  # this works for time and Date
    body = models.TextField()  # This works when we are dealing with body info description.
    url = models.TextField()
    image = models.ImageField(upload_to='images/', null=True)  # this is used to show out the image in our project.
    icon = models.ImageField(upload_to='images/', null=True)
    votes_total = models.IntegerField(default=1, null=True)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.email

    def summary(self):
        return self.body[:100]

    def pubdate_pretty(self):
        return self.pub_date.strftime('%b %e %Y')


# Products class
# tittle
# url
# pubdate
# votes_total
# image
# icon
# body
# pub_date_pretty
# hunter

class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name + '' + self.last_name


class Doctor(models.Model):
    DoctorProffesion = models.CharField(max_length=255)  # this has used to show title / heading
    Location = models.CharField(max_length=200)
    Sex = models.CharField(max_length=200)  # this works for time and Date
    Meeting_type = models.TextField(100)  # This works when we are dealing with body info description.

    def __str__(self):
        return self.DoctorProffesion

    def summary(self):
        return self.Location[:100]

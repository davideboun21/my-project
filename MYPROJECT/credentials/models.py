from django.db import models


class PersonalInformation(models.Model):
    name = models.CharField(max_length=100)
    contact_address = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    sex = models.BooleanField()
    nationality = models.CharField(max_length=20)


class InstitutionsAttended(models.Model):
    name = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    year = models.IntegerField()


class WorkExperience(models.Model):
    company_name = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    year = models.DateField()

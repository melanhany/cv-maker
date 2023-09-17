from django.db import models
from phonenumber_field.modelfields import PhoneNumberField  # type: ignore


class UserProfile(models.Model):
    # user field
    job_title: models.CharField = models.CharField(max_length=100)
    email: models.EmailField = models.EmailField()
    phone_number: PhoneNumberField = PhoneNumberField(blank=True)
    address: models.CharField = models.CharField(max_length=100, blank=True)
    image: models.ImageField = models.ImageField()


class Education(models.Model):
    # user field
    institution: models.CharField = models.CharField(max_length=255)
    degree: models.CharField = models.CharField(max_length=100)
    major: models.CharField = models.CharField(max_length=100)
    start_date: models.DateField = models.DateField()
    end_date: models.DateField = models.DateField()


class Experience(models.Model):
    # user field
    position: models.CharField = models.CharField(max_length=100)
    company_name: models.CharField = models.CharField(max_length=100)
    description: models.TextField = models.TextField()
    start_date: models.DateField = models.DateField()
    end_date: models.DateField = models.DateField()


class Skill(models.Model):
    # user field
    skill_name: models.CharField = models.CharField(max_length=100)
    proficiency: models.CharField = models.CharField(max_length=50)

from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField  # type: ignore


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name: models.CharField = models.CharField(max_length=100)
    last_name: models.CharField = models.CharField(max_length=100)
    job_title: models.CharField = models.CharField(max_length=100)
    email: models.EmailField = models.EmailField()
    phone_number: PhoneNumberField = PhoneNumberField(blank=True)
    address: models.CharField = models.CharField(max_length=100, blank=True)
    image: models.ImageField = models.ImageField(upload_to="cv/images")


class Education(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    institution: models.CharField = models.CharField(max_length=255)
    degree: models.CharField = models.CharField(max_length=100)
    major: models.CharField = models.CharField(max_length=100)
    start_date: models.DateField = models.DateField(blank=False, null=False)
    end_date: models.DateField = models.DateField(blank=False, null=False)


class Experience(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    position: models.CharField = models.CharField(max_length=100)
    company_name: models.CharField = models.CharField(max_length=100)
    description: models.TextField = models.TextField(blank=True)
    start_date: models.DateField = models.DateField(blank=False, null=False)
    end_date: models.DateField = models.DateField(blank=False, null=False)


class Skill(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    skill_name: models.CharField = models.CharField(max_length=100)
    proficiency: models.CharField = models.CharField(max_length=50)

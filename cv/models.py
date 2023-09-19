from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField  # type: ignore


class Resume(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class UserProfile(models.Model):
    resume = models.OneToOneField(Resume, on_delete=models.CASCADE)
    job_title: models.CharField = models.CharField(max_length=100)
    first_name: models.CharField = models.CharField(max_length=100)
    last_name: models.CharField = models.CharField(max_length=100)
    porfolio: models.URLField = models.URLField(max_length=255)
    email: models.EmailField = models.EmailField(blank=True)
    phone_number: PhoneNumberField = PhoneNumberField(blank=True)
    address: models.CharField = models.CharField(max_length=100, blank=True)
    image: models.ImageField = models.ImageField(upload_to="cv/images")


class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    institution: models.CharField = models.CharField(max_length=255)
    degree: models.CharField = models.CharField(max_length=100)
    major: models.CharField = models.CharField(max_length=100)
    start_date: models.DateField = models.DateField(blank=False, null=False)
    end_date: models.DateField = models.DateField(blank=False, null=False)


class Experience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    position: models.CharField = models.CharField(max_length=100)
    company_name: models.CharField = models.CharField(max_length=100)
    description: models.TextField = models.TextField(blank=True)
    start_date: models.DateField = models.DateField(blank=False, null=False)
    end_date: models.DateField = models.DateField(blank=False, null=False)


class Skill(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    name: models.CharField = models.CharField(max_length=100)
    proficiency: models.CharField = models.CharField(max_length=50)


class Language(models.Model):
    ELEMENTARY = "A1"
    PRE_ENTERMEDIATE = "A2"
    INTERMEDIATE = "B1"
    UPPER_ENTERMEDIATE = "B2"
    ADVANCED = "C1"
    PROFICIENT = "C2"
    NATIVE = "N"
    LANGUAGE_LEVEL_CHOICES = [
        (ELEMENTARY, "Elementary"),
        (PRE_ENTERMEDIATE, "Pre Intermediate"),
        (INTERMEDIATE, "Intermediate"),
        (UPPER_ENTERMEDIATE, "Upper Intermediate"),
        (ADVANCED, "Advanced"),
        (PROFICIENT, "Proficient"),
        (NATIVE, "Native"),
    ]

    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    name: models.CharField = models.CharField(max_length=50)
    level: models.CharField = models.CharField(
        max_length=2, choices=LANGUAGE_LEVEL_CHOICES, default=ELEMENTARY
    )

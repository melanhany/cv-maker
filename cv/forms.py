from django import forms
from django.conf import settings
from .models import UserProfile, Education, Experience, Skill, Language


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            "job_title",
            "first_name",
            "last_name",
            "porfolio",
            "email",
            "phone_number",
            "address",
            "image",
        ]
        # widgets = {"phone_number": forms.NumberInput(attrs={"type": "phone"})}


class EducationForm(forms.ModelForm):
    start_date = forms.DateField(
        input_formats=["%d-%m-%Y", "%d/%m/%Y", "%d/%m/%Y"],
        widget=forms.DateInput(attrs={"type": "date"}),
    )
    end_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))

    class Meta:
        model = Education
        exclude = ["resume"]


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        exclude = ["resume"]
        widgets = {
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "end_date": forms.DateInput(attrs={"type": "date"}),
        }


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        exclude = ["resume"]


class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        exclude = ["resume"]

from django import forms

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


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ["institution", "degree", "major", "start_date", "end_date"]


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ["position", "company_name", "description", "start_date", "end_date"]


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ["name", "proficiency"]


class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ["name", "level"]

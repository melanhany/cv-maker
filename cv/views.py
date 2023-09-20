from django.shortcuts import render


from .forms import (
    UserProfileForm,
    EducationForm,
    ExperienceForm,
    SkillForm,
    LanguageForm,
)


def user_profile_view(request):
    user_profile_form = UserProfileForm(request.POST or None)
    education_form = EducationForm()
    experience_form = ExperienceForm()
    skill_form = SkillForm()
    language_form = LanguageForm()
    # if user_profile_form.is_valid():
    #     user_profile_form.save()
    context = {
        "user_profile_form": user_profile_form,
        "education_form": education_form,
        "experience_form": experience_form,
        "skill_form": skill_form,
        "language_form": language_form,
    }
    return render(request, "cv/index.html", context)

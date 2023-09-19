from django.shortcuts import render


from .forms import UserProfileForm, EducationForm


def user_profile_view(request):
    user_profile_form = UserProfileForm(request.POST or None)
    education_form = EducationForm()

    # if user_profile_form.is_valid():
    #     user_profile_form.save()
    context = {"user_profile_form": user_profile_form, "education_form": education_form}
    return render(request, "cv/index.html", context)

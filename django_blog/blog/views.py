from django.shortcuts import render, redirect
from .forms import RegisterForm, ProfileForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages



def home(request):
    return render(request, 'blog/base.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {"form": form})


@login_required
def profile(request):
    user = request.user
    profile = getattr(user, 'profile', None)

    if request.method == 'POST':
        register_form = RegisterForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if register_form.is_valid() and profile_form.is_valid():
            register_form.save()  # updates email, names, etc.
            profile_form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
        else:
            messages.error(request, 'Please fix the errors below.')
    else:
        register_form = RegisterForm(instance=user)
        profile_form = ProfileForm(instance=profile)

    return render(request, 'blog/profile.html', {
        'register_form': register_form,
        'profile_form': profile_form,
    })
from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Authentication imports
from django.contrib.auth import authenticate, login, logout



def homepage(request):
    return render(request, 'blog/base.html')


#User Registration View
def user_registration(request):
    form = CreateUserForm()

    if request.method == 'POST':

        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            
            return redirect('user-login')

    context = {'registerform':form}

    return render(request, 'registration/register.html', context=context)



#User Login View
def user_login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                return redirect('dashboard')
            
    context = {'loginform':form}

    return render(request, 'registration/login.html', context=context)
        
    
#User LogoutView
def user_logout(request):
    logout(request)
    return redirect("")


@login_required(login_url='user-login')
#Dashboard
def dashboard(request):
    return render(request, 'blog/dashboard.html')



@login_required
def profile(request):
    user = request.user
    profile = getattr(user, 'profile', None)

    if request.method == 'POST':
        register_form = CreateUserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if register_form.is_valid() and profile_form.is_valid():
            register_form.save()  # updates email, names, etc.
            profile_form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
        else:
            messages.error(request, 'Please fix the errors below.')
    else:
        register_form = CreateUserForm(instance=user)
        profile_form = ProfileForm(instance=profile)

    return render(request, 'blog/profile.html', {
        'register_form': register_form,
        'profile_form': profile_form,
    })


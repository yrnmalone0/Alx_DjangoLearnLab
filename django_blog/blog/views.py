from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, ProfileForm, PostForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Authentication imports
from django.contrib.auth import authenticate, login, logout

from .models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy



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


#Dashboard View
@login_required(login_url='user-login')
def dashboard(request):
    return render(request, 'blog/dashboard.html')


# Profile View
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


# - Create Post View
class CreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/create_post.html'
     # Define the success URL after successful update
    success_url = reverse_lazy('posts') 

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

# - List Posts View
class ListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'


# - Detail Post View
class DetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


# - Update Post View    
class UpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/update_post.html'
     # Define the success URL after successful update
    success_url = reverse_lazy('posts')


# - Delete Post View
class DeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('posts')
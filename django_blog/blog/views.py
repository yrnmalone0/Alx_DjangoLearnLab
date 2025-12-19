from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, ProfileForm, PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Authentication imports
from django.contrib.auth import authenticate, login, logout

from .models import Post, Comment
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from taggit.models import Tag
from django.db.models import Q



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
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/creating_post.html'
     # Define the success URL after successful update
    success_url = reverse_lazy('posts') 

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

# - List Posts View
class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/listing_post.html'
    context_object_name = 'posts'


# - Detail Post View
class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'blog/viewing_post.html'
    context_object_name = 'post'


# - Update Post View    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/editing_post.html'
     # Define the success URL after successful update
    success_url = reverse_lazy('posts')

    
    def test_func(self):
        """
        This function checks whether the logged-in user is the author of the post.
        """
        post = self.get_object()
        return self.request.user == post.author


# - Delete Post View
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('posts')

    
    def test_func(self):
        """
        This function checks whether the logged-in user is the author of the post.
        """
        post = self.get_object()
        return self.request.user == post.author
    




# - Comment View
class CommentCreateView(LoginRequiredMixin,CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment.html'
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        form.instance.author = self.request.user
        post_id = self.kwargs['post_id']
        post = Post.objects.get(pk=post_id)
        form.instance.post = post
        return super().form_valid(form)
    

# Edit Comment View
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/edit_comment.html'
    success_url = reverse_lazy('posts')
    
    def test_func(self):
        """
        This function checks whether the logged-in user is the author of the comment.
        """
        comment = self.get_object()
        return self.request.user == comment.author
    
# List Comments View
class CommentListView(LoginRequiredMixin, ListView):
    model = Comment
    template_name = 'blog/listing_comments.html'
    context_object_name = 'comments'



# - Delete Comment View
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_delete.html'
    success_url = reverse_lazy('posts')

    
    def test_func(self):
        """
        This function checks whether the logged-in user is the author of the comment.
        """
        comment = self.get_object()
        return self.request.user == comment.author
    

# - Posts by Tag View
def posts_by_tag(request, tag_slug):
    tag = Tag.objects.get(slug=tag_slug)
    posts = tag.posts.all()  # This gets all posts related to the tag

    return render(request, 'blog/posts_by_tag.html', {'posts': posts, 'tag': tag})


# - Search Posts View
def search_posts(request):
    query = request.GET.get('q', '')  # Get the search query from the URL parameter
    if query:
        # Perform a case-insensitive search on title, content, and tags
        posts = Post.objects.filter(
            Q(title__icontains=query) |  # Search for query in the title
            Q(content__icontains=query) |  # Search for query in the content
            Q(tags__name__icontains=query)  # Search for query in the tags
        ).distinct()  # Ensures no duplicate posts are returned if they match multiple tags
    else:
        posts = Post.objects.all()  # If no query, return all posts

    return render(request, 'blog/search_results.html', {'posts': posts, 'query': query})
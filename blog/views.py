from django.shortcuts import render
from .models import Project, Post, Certificates
from django.views.generic import ListView, DetailView
from django.conf import settings
from django.core.mail import EmailMessage

def home(request):
    projects = Project.objects.all()
    posts = Post.objects.all()
    context = {'projects':projects, 'posts':posts}
    return render(request, 'blog/index.html', context)

def certificates(request):
    certificates = Certificates.objects.all()
    context = {'certificates':certificates}
    return render(request, 'blog/certificates.html', context)


def resume(request):
    return render(request, 'blog/resume.html')


class ProjectListView(ListView):
    model = Project
    template_name = 'blog/projects.html'
    context_object_name = 'projects'


class PostListView(ListView):
    model = Post
    template_name = 'blog/posts.html'
    context_object_name = 'posts'


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'blog/project_detail.html'
    context_object_name = 'project'
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_project = self.object
        previous_project = Project.objects.filter(date__lt=current_project.date).order_by('-date').first()
        next_project = Project.objects.filter(date__gt=current_project.date).order_by('date').first()

        context['previous_project'] = previous_project
        context['next_project'] = next_project
        return context


def contact(request):
    return render(request, 'blog/contact.html', {'title': 'Contact'})

def user_contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        contact_message = f"Name: {name}\nEmail: {email}\nMessage: {message}"
    
        email_message = EmailMessage(
            f'Message from {name}',
            contact_message,
            settings.EMAIL_HOST_USER,
            ['abrarshahriar360@yahoo.com'],
        )

        email_message.send()
    
        return render(request, 'blog/user_contact.html', {
            'name': name,
            'email': email,
            'message': message,
        })
    
    else:
        return render(request, 'blog/contact.html', {})

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_post = self.object
        previous_post = Post.objects.filter(date_posted__lt=current_post.date_posted).order_by('-date_posted').first()
        next_post = Post.objects.filter(date_posted__gt=current_post.date_posted).order_by('date_posted').first()

        context['previous_post'] = previous_post
        context['next_post'] = next_post
        return context
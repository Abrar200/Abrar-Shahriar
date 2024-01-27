from django.urls import path
from . import views
from .views import ProjectListView, ProjectDetailView, PostListView, PostDetailView

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', ProjectListView.as_view(), name='projects'),
    path('blog/', PostListView.as_view(), name='blog'),
    path('projects/<slug:slug>', ProjectDetailView.as_view(), name='project-detail'),
    path('blog/<slug:slug>', PostDetailView.as_view(), name='post-detail'),
    path('contact/', views.contact, name='contact'),
    path('user-contact/', views.user_contact, name='user-contact'),
    path('certificates/', views.certificates, name='certificates'),
    path('resume/', views.resume, name='resume'),
]
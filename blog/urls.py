from django.urls import path
from . import views
from .views import contact, success

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('contact/', views.contact, name='blog-contact'),
    path('files/', views.files, name='blog-files'),
    path('about/', views.about, name='blog-about'),
    path('success/', views.success, name='blog-success'),
]

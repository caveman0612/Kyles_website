from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('pdf_resume/', views.pdf_resume, name='pdf_resume'),
    path('projects', views.projects, name='projects'),
]
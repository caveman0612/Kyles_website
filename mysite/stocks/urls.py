from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_page, name='start_page'),
    path('companies/', views.companies, name='companies'),
    path('company_name/', views.company_name, name='company_name')
]
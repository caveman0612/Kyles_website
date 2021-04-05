from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_page, name='start_page'),
    path("short_list/", views.short_list, name="short list"),
    path('companies/', views.companies, name='companies'),
    path('company_name/', views.company_name, name='company_name')
    # path('stocks/short_list/', views.short_list, name="short list")
]
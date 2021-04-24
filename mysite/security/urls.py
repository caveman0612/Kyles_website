from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('zones/', views.zones, name="zones"),
    path('employees/', views.employees, name="employees"),
    path('weather/', views.weather, name="weather")
]
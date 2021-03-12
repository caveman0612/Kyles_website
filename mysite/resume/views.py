from django.shortcuts import render
from django.http import HttpResponse

def landing_page (response):
    return HttpResponse("<h1>This is the landing page</h1>")

def pdf_resume (response):
    return HttpResponse("<h1> PDF RESUME </h1>")

def projects (response):
    return HttpResponse("<h1> Projects </h1>")

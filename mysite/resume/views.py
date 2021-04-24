from django.shortcuts import render
from django.http import HttpResponse

# mysite/resume/templates/resume/home.html

def landing_page (response):
    return render(response, "resume/home.html")

def pdf_resume (response):
    return render(response, "resume/PDF_resume.html")

def projects (response):
    return render(response, "resume/projects.html")

def bio (response):
    return render(response, "resume/bio.html")

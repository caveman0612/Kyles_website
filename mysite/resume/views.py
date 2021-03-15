from django.shortcuts import render
from django.http import HttpResponse

# mysite/resume/templates/resume/landing_page.html

def landing_page (response):
    return render(response, "resume/landing_page.html")

def pdf_resume (response):
    return render(response, "resume/PDF_resume.html")

def projects (response):
    return render(response, "resume/projects.html")

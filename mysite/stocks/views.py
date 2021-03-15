from django.shortcuts import render
from django.http import HttpResponse

def companies (response):
    return render(response, "stocks/companies.html")

def start_page(response):
    return render(response, "stocks/start_page.html")

def company_name(response):
    return render(response, "stocks/company_name.html")

from django.shortcuts import render
from django.http import HttpResponse

def companies (response):
    return HttpResponse("<h1> list of companies</h1>")

def start_page(response):
    return HttpResponse("<h1> Stocks start page</h1>")

def company_name(response):
    return HttpResponse("<h1> Individual companies would go here </h1>")

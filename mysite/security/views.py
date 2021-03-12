from django.shortcuts import render
from django.http import HttpResponse

def main(response):
    HttpResponse("<h1> The main screen with the google maps </h1>")

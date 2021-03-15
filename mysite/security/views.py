from django.shortcuts import render
from django.http import HttpResponse

def main(response):
    return render(response, "security/sec_main.html")
    # return HttpResponse("<h1> The main screen with the google maps </h1>")

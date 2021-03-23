from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import NameForm

def companies (response):
    return render(response, "stocks/companies.html")

def start_page(response):
    #make instance of form
    if response.method == "POST":
        form = NameForm(response.POST)
        if form.is_valid():
            return HttpResponseRedirect('/stocks/thanks/')
    else:
        form = NameForm()

    return render(response, "stocks/start_page.html", {'form': form})
    # return render(response, "stocks/start_page.html")

def company_name(response):
    return render(response, "stocks/company_name.html")

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import NameForm
from.models import ListOfCompanies, Company

def companies (response):
    # ls = ListOfCompanies.objects.get(id=1)
    # item = ls.company_set.get(id=1)
    # return render(response, "stocks/start_page.html", {"ls": ls})
    return render(response, "stocks/companies.html")

def short_list(response):
    ls = ListOfCompanies.objects.get(id=1)

    if response.method == "POST":
        if response.POST.get("save"):
            for item in ls.company_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                item.save()
        elif response.POST.get("newItem"):
            txt = response.POST.get("new")

            if len(txt) > 2:
                ls.company_set.create(text=txt, complete=False)
            else:
                print("invalid")
    # item = ls.company_set.get(id=1) "item": item}
    return render(response, "stocks/short_list.html", {"ls":ls})

def long_hold(response):
    ls = ListOfCompanies.objects.get(id=2)
    item = ls.company_set.get(id=1)
    return render(response, "stocks/short_list.html", {"ls":ls, "item": item})

def day_trading(response):
    ls = ListOfCompanies.objects.get(id=3)
    item = ls.company_set.get(id=1)
    return render(response, "stocks/short_list.html", {"ls":ls, "item": item})

def start_page(response):

    return render(response, "stocks/start_page.html")

    # return HttpResponse("<h1>%s</h1><br><p>%s</p>" %(ls.name, str(item.text)))

    # return render(response, "stocks/start_page.html", {'form': form})


def company_name(response):
    return render(response, "stocks/company_name.html")


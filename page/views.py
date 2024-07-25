from django.shortcuts import render, HttpResponse
from random import randint
# Create your views here.
def home(request):
    title = "Index"
    content = {"platform": f"Django framework kullanıldı ... {randint(1,100)}", title:title}

    return render(request, "page/index.html", content)

def contact_us_view(request):
    content = dict()
    return render(request,"page/contact_us.html", content)

def about_us_view(request):
    content=dict()
    return render(request, "page/about_us.html", content)

def vision_view(request):
    content=dict()
    return render(request, "page/vision.html", content)
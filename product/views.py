from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def product(request):
    template=loader.get_template("product.html")
    data={"name":"redmi",
          "Desc":"Smartphone"}
    return HttpResponse(template.render(data,request))
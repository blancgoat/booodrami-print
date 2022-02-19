from django.shortcuts import render
from django.http import HttpResponse
import os 

# Create your views here.
def index(request):
    os.system("wkhtmltopdf --page-width 150mm --page-height 100mm http://localhost:8000/pdf  wow.pdf")
    return HttpResponse("wow")
from django.shortcuts import render, HttpResponse
from . import templates


# Create your views here.

def home(request):
    context = {'tvar': 'tvar'}
    return render(request, "index.html", context)

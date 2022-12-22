from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def gamze(request):
    return HttpResponse("Hello application:)")

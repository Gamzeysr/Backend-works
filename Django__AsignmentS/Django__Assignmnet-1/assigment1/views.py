from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home (request):
    return HttpResponse('This is our home page....')

    # 3.Adım
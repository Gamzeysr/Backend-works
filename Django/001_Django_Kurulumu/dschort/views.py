from django.shortcuts import render
from django.shortcuts import HttpResponse



# Create your views here.
def beginner(request):
    return HttpResponse('how are you:)')

from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse ("Welcome backend")

#! view i bir beyin gibi düşün! 
#! frontendin isteği neyse onu burada bir fonksiyon gibi çalıştıracak.
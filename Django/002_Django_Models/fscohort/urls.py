from django.urls import path
from fscohort.views import home
 
urlpatterns = [
    path("fscohort",home),
    
]
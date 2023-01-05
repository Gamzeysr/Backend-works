from django.http import HttpResponse

def real_home(request):
    return HttpResponse('This main home page......')

    #!✨ anasayfa da görüneceginden burada yani main de view dosyası olusturup urls.py de pathı beklirledim 
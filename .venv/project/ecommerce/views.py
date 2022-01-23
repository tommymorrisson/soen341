from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, SOEN 341 Group!")

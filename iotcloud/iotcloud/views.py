from django.http import HttpResponse

def home(request):
    return HttpResponse("<a href='/dashboard'> GO TO DASHBOARD <a>")
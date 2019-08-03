from django.shortcuts import render
from django.http import HttpResponse
from .models import Buttons
from django.shortcuts import redirect

# Create your views here.
def dashboard(request):
    stats = Buttons.objects.all()
    for stat in stats:
        tt = str(stat.number) + ":" +stat.status
        print(tt)
    return render(request,'iot_control/dashboard.html')

def toggle(request):
    num = request.GET.get('num')
    sta = request.GET.get('sta')
    stats = Buttons.objects.all()
    for stat in stats:
        if str(stat.number)==str(num):
            stat.status = sta
            stat.save()
    #return redirect('/dashboard')
    return HttpResponse(stats)
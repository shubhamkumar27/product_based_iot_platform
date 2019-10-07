from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from .models import P4node,P8node,Extendeduser
from django.shortcuts import redirect
from django.contrib import messages

###################################################

@login_required(login_url='/login/')
def dashboard(request):
    pid = ''
    ptype = ''
    if Extendeduser.objects.filter(user = request.user).exists():
        userdetail = Extendeduser.objects.filter(user = request.user)
        for d in userdetail:
            pid = d.product_id
            ptype = d.product_type
        param = {'pid': pid}
        if ptype=='4-NODE':
            return render(request, 'p4dash.html', param)
        if ptype=='8-NODE':
            return render(request, 'p8dash.html', param)
    # stats = P8node.objects.all()
    # for stat in stats:
    #     tt = str(stat.number) + ":" +stat.status
    #     print(tt)
    # param = {'relay1':1}
    else:
        return render(request,'devregister.html')

def p4toggle(request):
    num = request.GET.get('num')
    sta = request.GET.get('sta')
    stats = P8node.objects.all()
    for stat in stats:
        if str(stat.number)==str(num):
            stat.status = sta
            stat.save()
    #return redirect('/dashboard')
    return HttpResponse(stats)

def p8toggle(request):
    num = request.GET.get('num')
    sta = request.GET.get('sta')
    stats = P8node.objects.all()
    for stat in stats:
        if str(stat.number)==str(num):
            stat.status = sta
            stat.save()
    #return redirect('/dashboard')
    return HttpResponse(stats)

@login_required(login_url='/login/')
def devregister(request):
    phn = request.POST.get('phone')
    product_id = request.POST.get('product_id')
    type = request.POST.get('type')
    if str(type)=='8NODE':
        if P8node.objects.filter(product_id=product_id).exists():
            a = P8node.objects.filter(product_id=product_id)
            print(a.username)
            print('yes')
        else:
            print('product not found')
            messages.info(request, 'Device not found !!')
            return redirect('/dashboard/')
    if str(type)=='4NODE':
        if P4node.objects.filter(product_id=product_id).exists():
            print('yes')
        else:
            print('product not found')
            messages.info(request, 'Device not found !!')
            return redirect('/dashboard/')
    if Extendeduser.objects.filter(product_id=product_id).exists():
        messages.info(request, 'Device already registered !!')
        return redirect('/dashboard/')
    print(type)
    exuser = Extendeduser(user=request.user, product_id=product_id, product_type=type, phone_num=phn)
    exuser.save()
    return redirect('/dashboard/')
#############

from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.template import loader,RequestContext
from django.http import HttpResponse
from .models import *
# Create your views here.


def index(request):
    articles=Anli.objects.all()
    pad=Advise.objects.all()
    img=Img.objects.all()
    temp=team.objects.all()
    return render(request,'index.html',locals())

def detail(request,id):
        articles=get_object_or_404(Anli,pk=id)

        return render(request,'detail.html',locals())

def jointeam(request):
    if request.method=='GET':
        return render(request,'jointeam.html')
    else:
        username=request.POST.get('username')
        email = request.POST.get('email')
        work = request.POST.get('work')
        error='提交成功，请等待审批。'
        return render(request,'jointeam.html',{'error':error})

def services(request):
    server=service.objects.all()
    han=type_on.objects.all()

    return render(request,'services.html',locals())

def bill(request,id):
    pirce = get_object_or_404(type_on, pk=id)
    if request.method=='GET':
        return render(request,'bill.html',{'pirce':pirce})
    elif request.method=='POST':
        return render(request,'bill.html',{'pirce':pirce,'error':'以下订单，请等待验收'})


def itemn(request):
    items=item.objects.all()
    return render(request,'portfolio.html',locals())

def itemsingle(request,id):
    items=get_object_or_404(item,pk=id)
    itemtys=get_object_or_404(itemtype,pk=id)
    return render(request,'portfolio-single.html',locals())

# 联系
def contact(request):
    return render(request,'contact.html')

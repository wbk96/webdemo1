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
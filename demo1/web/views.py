from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.template import loader,RequestContext
from django.http import HttpResponse
from django.core.mail import send_mail, send_mass_mail
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
    if request.method=='GET':
        return render(request,'contact.html')
    else:
        name=request.POST.get('name')
        work=request.POST.get('work')
        email=request.POST.get('email')
        misg=request.POST.get('massige')
        try :

            from django.conf import settings
            send_mail(name,misg,settings.DEFAULT_FROM_EMAIL,['1774678547@qq.com'])
            return render(request,'contact.html',{'error':'邮件发送成功'})
        except Exception as e:
            print(e)
            return render(request,'contact.html',{'error':'邮件发送失败'})


#博客
def blog(request):
    articles=Article.objects.all()
    categorys=Category.objects.all()
    arts=Article.objects.order_by('-creater_time')
    return render(request,'blog.html',locals())

#博客文章详情页
def blogsingle(request,id):
    articles=Article.objects.get(pk=id)
    categorys = Category.objects.all()
    arts = Article.objects.order_by('-creater_time')
    comments = comment.objects.filter(article=id).all()
    if request.method=='GET':
        return render(request, 'blog-single.html', locals())
    elif request.method=='POST':
        user=comment()
        user.title=request.POST.get('name')
        user.email=request.POST.get('email')
        user.body=request.POST.get('talk')
        user.article_id=id
        user.save()
        return render(request,'blog-single.html')

#右边的
def blogdetail(request,id):
    cat=get_object_or_404(Category,pk=id)
    articles=cat.article_set.all()
    return render(request,'blogdetail.html',locals())

#所有
def allblog(request):
    articles = Article.objects.all()
    return render(request,'allblog.html',locals())
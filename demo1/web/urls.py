from django.conf.urls import url
from . import views

app_name='web'
urlpatterns = [
    url(r'^index/$',views.index,name='index'),
    url(r'^detail/(\d+)/$',views.detail,name='detail'),
    url(r'^jointeam/$',views.jointeam,name='jointeam'),
    url(r'^services/$',views.services,name='services'),
    url(r'^bill/(\d+)/$',views.bill,name='bill'),
    url(r'^itemn/$',views.itemn,name='itemn'),
    url(r'^itemsingle/(\d+)/$',views.itemsingle,name='itemsingle'),
    url(r'^contact/$',views.contact,name='contact'),
    url(r'^blog/$',views.blog,name='blog'),
    url(r'^blogsingle/(\d+)/$',views.blogsingle,name='blogsingle'),
    url(r'^blogdetail/(\d+)/$',views.blogdetail,name='blogdetail'),
    url(r'^allblog/$',views.allblog,name='allblog'),
]
from django.db import models

# Create your models here.

# 首页案例
class Anli(models.Model):
    title=models.CharField(max_length=20,verbose_name='标题')
    body=models.CharField(max_length=500,verbose_name='内容')
    img=models.ImageField(upload_to='abs',verbose_name='图片')
    def __str__(self):
        return self.title
    class Meta():
        verbose_name='文章'
        verbose_name_plural=verbose_name
#用户建议
class Advise(models.Model):
    title=models.CharField(max_length=20,verbose_name='客户名')
    post=models.CharField(max_length=20,verbose_name='职位')
    body=models.CharField(max_length=500,verbose_name='意见')
    img=models.ImageField(upload_to='abs')
    def __str__(self):
        return self.title
    class Meta():
        verbose_name = '客户意见'
        verbose_name_plural = verbose_name
#图片集
class Img(models.Model):
    img=models.ImageField(upload_to='ads')
    class Meta():
        verbose_name = '图片集'
        verbose_name_plural = verbose_name

#团队
class team(models.Model):
    title=models.CharField(max_length=20,verbose_name='公司名')
    post=models.CharField(max_length=20,verbose_name='职位')
    body=models.CharField(max_length=100,verbose_name='简介')
    img=models.ImageField(upload_to='abs')

    class Meta():
        verbose_name = '团队'
        verbose_name_plural = verbose_name

#加入团队
class Join(models.Model):
    pass

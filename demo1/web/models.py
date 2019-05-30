from django.db import models


# Create your models here.

# 首页案例
class Anli(models.Model):
    title = models.CharField(max_length=20, verbose_name='标题')
    body = models.CharField(max_length=500, verbose_name='内容')
    img = models.ImageField(upload_to='abs', verbose_name='图片')

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = '文章'
        verbose_name_plural = verbose_name


# 用户建议
class Advise(models.Model):
    title = models.CharField(max_length=20, verbose_name='客户名')
    post = models.CharField(max_length=20, verbose_name='职位')
    body = models.CharField(max_length=500, verbose_name='意见')
    img = models.ImageField(upload_to='abs')

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = '客户意见'
        verbose_name_plural = verbose_name


# 图片集
class Img(models.Model):
    img = models.ImageField(upload_to='ads')

    class Meta():
        verbose_name = '图片集'
        verbose_name_plural = verbose_name


# 团队
class team(models.Model):
    title = models.CharField(max_length=20, verbose_name='公司名')
    post = models.CharField(max_length=20, verbose_name='职位')
    body = models.CharField(max_length=100, verbose_name='简介')
    img = models.ImageField(upload_to='abs')

    class Meta():
        verbose_name = '团队'
        verbose_name_plural = verbose_name


# 服务外键
class type_on(models.Model):
    type = models.CharField(max_length=30, verbose_name='类型')
    price = models.IntegerField()
    time = models.CharField(max_length=30, verbose_name='时长')

    class Meta():
        verbose_name = '服务类型'
        verbose_name_plural = verbose_name


# 服务
class service(models.Model):
    title = models.CharField(max_length=30, verbose_name='应用名')
    body = models.CharField(max_length=50, verbose_name='应用介绍')
    type = models.ForeignKey(type_on, on_delete=models.CASCADE)

    class Meta():
        verbose_name = '服务'
        verbose_name_plural = verbose_name


# 项目展示
class item(models.Model):
    title = models.CharField(max_length=30, verbose_name='项目名称')
    body = models.CharField(max_length=500, verbose_name='简介')
    img = models.ImageField(upload_to='abs')
    time = models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name = '项目'
        verbose_name_plural = verbose_name


# 项目相关图片
class itemimg(models.Model):
    img = models.ImageField(upload_to='abs')
    itimg = models.ForeignKey(item, on_delete=models.CASCADE)

    class Meta():
        verbose_name = '项目图片'
        verbose_name_plural = verbose_name


# 项目类型
class itemtype(models.Model):
    ittype = models.CharField(max_length=30, verbose_name='项目类型')
    itm = models.ForeignKey(item, on_delete=models.CASCADE)

    class Meta():
        verbose_name = '项目类型'
        verbose_name_plural = verbose_name

# 博客分类
class Category(models.Model):
    title = models.CharField(max_length=20, verbose_name='博客类型')

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = '博客类型'
        verbose_name_plural = verbose_name


# 博客文章
class Article(models.Model):
    auto=models.CharField(max_length=20,verbose_name='作者')
    title = models.CharField(max_length=30, verbose_name='文章')
    body = models.TextField()
    creater_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0)
    img=models.ImageField(upload_to='abs')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = '博客文章'
        verbose_name_plural = verbose_name

#博客评论
class comment(models.Model):
    title=models.CharField(max_length=30,verbose_name='姓名')
    email=models.EmailField(blank=True,null=True)
    body=models.CharField(max_length=500,verbose_name='评论')
    create_time=models.DateTimeField(auto_now_add=True)
    article=models.ForeignKey(Article,on_delete=models.CASCADE)

    class Meta():
        verbose_name = '博客评论'
        verbose_name_plural = verbose_name

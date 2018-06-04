from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name='昵称',default='')
    birthday = models.DateField(verbose_name='生日', blank=True, null=True)
    gender = models.CharField(choices=(('male', '男'),('female','女')),max_length=10, default='female')
    address = models.CharField(max_length=100, default='')
    moblie = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to='image/%Y/%m', default='image/default.png', max_length=100)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural= verbose_name

    def __str__(self):
        return self.username

class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name='验证码')
    email= models.EmailField(max_length=50, verbose_name='邮箱')
    send_type = models.CharField(verbose_name='发送验证类型', max_length=20,choices=(('register', '注册'),('forget','忘记密码')), default='')
    send_time = models.DateTimeField(verbose_name='发送时间', default=datetime.now)
    # HINT: It seems you set a fixed date / time / datetime value as default for this field  必须把上面的datetime.now()改成datetime.now

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name  # #verbose_name_plural 是复数形式，不设置的话，则默认增加一个s

    def __str__(self):
        return '{0}{1}'.format(self.code,self.email)

class Banner(models.Model):
    tittle = models.CharField(max_length=100, verbose_name='标题', default='')
    image = models.ImageField(upload_to='banner/%Y/%m', verbose_name='轮播图片')
    url = models.URLField(max_length=200, verbose_name='访问地址')
    index = models.IntegerField(default=100, verbose_name='序号')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name
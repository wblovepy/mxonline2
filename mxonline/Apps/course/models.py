from django.db import models
from datetime import datetime
from organizition.models import CourseOrg

# Create your models here.


class Course(models.Model):
    course_org = models.ForeignKey(CourseOrg,verbose_name='所属机构',on_delete=models.CASCADE,null=True, blank=True)  # null=True针对以前添加的字段，可以运行为空
    name = models.CharField(max_length=50, verbose_name='课程')
    description = models.CharField(max_length=300, verbose_name='课程描述')
    detail = models.TextField(verbose_name= '课程详情')
    degree = models.CharField(verbose_name='难易程度', max_length=20, choices=(('cj','初级'),('zj','中级'),('gj','高级')))
    learn_times = models.IntegerField(default=0, verbose_name='学习时长(分)')
    students = models.IntegerField(default=0, verbose_name='学习人数')
    fav_nums = models.IntegerField(default=0, verbose_name='收藏人数')
    image = models.ImageField(upload_to='course/%Y/%m', verbose_name='课程图片')
    click_num = models.IntegerField(default=0, verbose_name='课程点击数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='课程')  # 通过外键连接课程表
    name = models.CharField(max_length=100, verbose_name='章节名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name= '章节'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Video(models.Model):   # 视频播放地址
    lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE, verbose_name='章节' )
    name = models.CharField(max_length=100, verbose_name='视频名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '视频'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class CourseResource(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE, verbose_name='课程')
    name = models.CharField(max_length=100, verbose_name='资源名称')
    download = models.FileField(upload_to='course/resource/%Y/%m', verbose_name='资源')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '课程资源'
        verbose_name_plural = verbose_name
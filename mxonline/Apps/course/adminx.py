import xadmin
from .models import Course, Lesson, Video, CourseResource


class CourseAdmin(object):
    #  字段必须和models中定义一样，否则后台网页不能打开
    list_display = ['name', 'description', 'detail', 'degree', 'learn_times','students',
                    'fav_nums','image', 'click_num', 'add_time']
    search_fields = ['name', 'description', 'detail', 'degree', 'learn_times','students',
                    'fav_nums','image', 'click_num']
    list_filter = ['name', 'description', 'detail', 'degree', 'learn_times','students',
                    'fav_nums','image', 'click_num', 'add_time']


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']  # 显示那些字段，必须和model一样
    search_fields = ['course', 'name']  # 空白搜索框，可以输入的字段
    list_filter = ['course__name', 'name', 'add_time'] # 下拉过滤框可以收缩的字段，course是外键，必须制定course的具体字段才能正常显示，需要加两个下划线


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name', 'download']
    list_filter = ['course', 'name', 'download', 'add_time']


# 此处顺序和网页上显示顺序一致的
xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
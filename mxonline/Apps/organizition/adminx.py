import xadmin
from .models import  CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']

class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'click_nums','fav_nums','image','address','city', 'add_time'] # ‘’内都不能多一个空格
    search_fields = ['name', 'desc', 'click_nums','fav_nums','image','address','city']
    list_filter = ['name', 'desc', 'click_nums','fav_nums','image','address','city__name', 'add_time']
    raw_id_fields = ("city",)


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years','company', 'position','points','click_nums', 'fav_nums','add_time']
    search_fields = ['org', 'name', 'work_years','company', 'position','points','click_nums', 'fav_nums']
    list_filter = ['org', 'name', 'work_years','company', 'position','points','click_nums', 'fav_nums','add_time']
    raw_id_fields = ("org",)


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
from django.shortcuts import render
from django.views.generic import View
from organizition.models import CityDict,CourseOrg
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from .forms import AnotherUserForm
from django.http import HttpResponse
import json
from operation.models import UserFav
from course.models import Course
from .models import Teacher
# Create your views here.

class OrgListView(View):
    """
    课程机构列表功能
    """
    def get(self, request):
        all_org = CourseOrg.objects.all()
        # 根据点击量进行排名#
        hot_org = all_org.order_by("-click_nums")

        # org_num = all_org.count()
        # 类别筛选 #
        catgory = request.GET.get('ct', "")
        if catgory:
            all_org = all_org.filter(catgory=catgory)

        # 对城市进行筛选 #
        city_id = request.GET.get('city', "")
        if city_id:
            all_org = all_org.filter(city_id=city_id)
        org_num = all_org.count()
        # 对 all_org 进行排序 #
        sort =request.GET.get("sort")
        if sort =="student":
            all_org = all_org.order_by("-student")
        elif sort == "course_num":
            all_org = all_org.order_by("-course_num")

        # 对org_list进行分页 #
        try:
            page = request.GET.get('page', 1)  # 先选取某一页
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_org, 5, request=request)  # per_page=5是必填项
        orgs =p.page(page)  #  第page页的数据
        all_city = CityDict.objects.all()
        return  render(request, "org-list.html", {
            # "all_org":org_list,
            "all_city":all_city,
            "org_num":org_num,
            "all_org": orgs,
            "city_id":city_id,
            "catgory":catgory,
            "hot_org":hot_org,
            "sort":sort,
        })


class Add_askView(View):
    """用户参加咨询的Ajax操作"""
    """有个bug，号码为空的时候不响应"""
    def post(self,request):
        userask_form =AnotherUserForm(request.POST)
        if userask_form.is_valid():
            user_ask =userask_form.save(commit=True)
            # 一定要把提示转换成JSON的数据
            return HttpResponse(json.dumps({'status':'success'}),content_type='application/json')

        else:
            return HttpResponse(json.dumps({'status':'fail','msg':'提交错误'}), content_type='application/json')


class OrgHomePageView(View):
    def get(self, request, org_id):
        current_page ='home'
        """
        以下三句判断初始情况下用户是否已经收藏，并修改响应的显示，这样刷新页面时不会更改
        """
        has_fav= False
        if request.user.is_authenticated:
            if UserFav.objects.filter(user=request.user, fav_id=org_id, fav_type=2):
                has_fav =True
        course_org = CourseOrg.objects.get(id=int(org_id))  # 用fliter返回数组,需要遍历才能行，get返回对象
        all_course = course_org.course_set.all()[:3]  # 通过一个查询多个，一个course_org通过方法，将关联的表名全小写加上“_set”组成的方法
        all_teacher = course_org.teacher_set.all()[:1]
        # all_course=Course.objects.filter(course_org=org_id) [:3] # 通过fliter反向查询
        # all_teacher = Teacher.objects.filter(org=org_id).order_by('-click_nums')[:1]
        teacher_this_course= []
        return  render(request,"org-detail-homepage.html",{
            'all_course':all_course,
            'all_teacher':all_teacher,
            'course_org':course_org,
            'current_page':current_page,
            'has_fav':has_fav
        })

class OrgCourseView(View):
    def get(self,request,org_id):
        current_page = 'course'
        """
                以下三句判断初始情况下用户是否已经收藏，并修改响应的显示，这样刷新页面时不会更改
                """
        has_fav = False
        if request.user.is_authenticated:
            if UserFav.objects.filter(user=request.user, fav_id=org_id, fav_type=2):
                has_fav = True
        course_org = CourseOrg.objects.get(id=int(org_id))  # 用fliter返回数组,需要遍历才能行，get返回对象
        all_course = course_org.course_set.all()  # 通过一个查询多个，一个course_org通过方法，将关联的表名全小写加上“_set”组成的方法
        return render(request, "org-detail-course.html", {
            'all_course': all_course,
            'course_org': course_org,
            'current_page':current_page,
            "has_fav":has_fav,
        })


class OrgDescView(View):
    def get(self,request,org_id):
        current_page = 'desc'
        """
                以下三句判断初始情况下用户是否已经收藏，并修改响应的显示，这样刷新页面时不会更改
                """
        has_fav = False
        if request.user.is_authenticated:
            if UserFav.objects.filter(user=request.user, fav_id=org_id, fav_type=2):
                has_fav = True
        course_org = CourseOrg.objects.get(id=int(org_id))  # 用fliter返回数组,需要遍历才能行，get返回对象
        desc = course_org.desc  # 通过一个查询多个，一个course_org通过方法，将关联的表名全小写加上“_set”组成的方法
        return render(request, "org-detail-desc.html", {
            'desc': desc,
            'course_org': course_org,
            'current_page':current_page,
            "has_fav":has_fav,
        })


class OrgTeacherView(View):
    def get(self,request,org_id):
        current_page = 'teacher'
        """
                以下三句判断初始情况下用户是否已经收藏，并修改响应的显示，这样刷新页面时不会更改
                """
        has_fav = False
        if request.user.is_authenticated:
            if UserFav.objects.filter(user=request.user, fav_id=org_id, fav_type=2):
                has_fav = True
        course_org = CourseOrg.objects.get(id=int(org_id))  # 用fliter返回数组,需要遍历才能行，get返回对象
        all_teacher = course_org.teacher_set.all()  # 通过一个查询多个，一个course_org通过方法，将关联的表名全小写加上“_set”组成的方法
        return render(request, "org-detail-teachers.html", {
            'all_teacher': all_teacher,
            'course_org': course_org,
            'current_page':current_page,
            "has_fav":has_fav,
        })

class AddFavView(View):
        """对用户收藏与取消收藏进行Ajax操作"""
        def post(self, request):
            fav_id = request.POST.get('fav_id',0)
            fav_type =request.POST.get('fav_type',0)

            if not request.user.is_authenticated: # 未登陆时，是匿名用户,不能再后面加（）
                return HttpResponse(json.dumps({'status':'fail','msg':'用户未登陆'}),content_type='application/json')
            # 如果已经登陆，则查看是否收藏
            exist_records = UserFav.objects.filter(user=request.user, fav_id=int(fav_id), fav_type=int(fav_type))
            # UserFav.objects.get报错：UserFav matching query does not exist. 当get不到时就会报错。fliter会返回空数组
            if exist_records:
                exist_records.delete()
                return HttpResponse('{"status":"success","msg":"收藏"}', content_type='application/json')
            else:
                user_fav=UserFav()
                if int(fav_id) >0 and int(fav_type)>0:  # 因为默认是0，没有取到就是0，取到了就是字符串数值
                    user_fav.fav_id = int(fav_id)
                    user_fav.fav_type = int(fav_type)
                    user_fav.user = request.user
                    user_fav.save()
                    return HttpResponse('{"status":"success","msg":"已收藏"}', content_type='application/json')
                else:
                    return  HttpResponse('{"status":"fail","msg":"收藏出错"}', content_type='application/json')

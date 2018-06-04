from django.urls import path,include,re_path
from .views import OrgListView,Add_askView,OrgHomePageView,OrgCourseView,OrgDescView,OrgTeacherView,AddFavView


urlpatterns = [
    path('list/', OrgListView.as_view(), name='list'),
    path(r'add_ask/', Add_askView.as_view(),name='add_ask'),
    # path(r'homepage/', OrgHomePageView1.as_view(),name='homepage'),
    re_path(r'homepage/(?P<org_id>\d+)$',OrgHomePageView.as_view(),name='homepage'),
    re_path(r'course/(?P<org_id>\d+)$', OrgCourseView.as_view(),name='course'),
    re_path(r'desc/(?P<org_id>\d+)$', OrgDescView.as_view(),name='desc'),
    re_path(r'teacher/(?P<org_id>\d+)$', OrgTeacherView.as_view(),name='teacher'),
    path(r'add_fav/', AddFavView.as_view(),name='add_fav'),
]
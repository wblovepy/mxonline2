"""mxonline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
import xadmin
from django.views.static import serve
from django.views.generic import TemplateView
from user.views import LoginView,RegisterView,ActiveView,ForgetpwdView,ResetView, ModifyPwd, LogoutView
from organizition.views import OrgListView
from .settings import MEDIA_ROOT


urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('index/', TemplateView.as_view(template_name='index.html'),name = 'index'),
    path('login/', LoginView.as_view(), name = 'login'),
    path('register/', RegisterView.as_view(),name = 'register'),
    path('forgetpwd/',ForgetpwdView.as_view() , name='forgetpwd'),
    path(r'captcha/', include('captcha.urls')),
    re_path(r'active/(?P<active_code>.*)', ActiveView.as_view(),name ='active'), #
    re_path(r'modifypwd/$', ModifyPwd.as_view(), name ='modify_pwd'),
    re_path(r'reset/(?P<reset_code>.*)$', ResetView.as_view(), name ='reset'),
    path(r'logout/', LogoutView.as_view(), name= 'logout'),
    # path(r'org_list/', OrgListView.as_view(), name='org_list'),
    path(r'org/', include(('organizition.urls','organizition'), namespace='org')),  # namespace 需要提供app名字，要不然就会报错
    # 上传用户文件的路径#

    re_path(r'media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    ]
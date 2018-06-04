from django.shortcuts import render,redirect
from user.models import UserProfile
from django.contrib.auth import authenticate,login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic import View
from user.forms import LoginForm, RegisterForm, ForgetpwdForm, ModifyPwdForm
from user.models import EmailVerifyRecord
from django.contrib.auth.hashers import make_password
from utils.email_send import send_register_email
# Create your views here.


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user= UserProfile.objects.get(Q(username=username)|Q(email=username))  # 返回的是 userprofile.name
            if user.check_password(password):
                return user
        except Exception as E:
            return None


class LoginView(View):
    """用类的方法重写login"""
    def get(self, request):
        return render(request, "login.html", {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            user = authenticate(username=user_name,
                                password=pass_word)  # 首先进行验证，If the given credentials are valid, return a User object.
            if user is not None:
                if user.is_active:
                    login(request, user)
                    is_authenticated = request.user.is_authenticated
                    return render(request, 'index.html', {"is_authenticated": is_authenticated, "username": user})
                    # return redirect("/index", {"is_authenticated": True, "username":user})  # redirect不能传递参数吗？
                else:
                    return render(request, 'login.html', {"msg": '用户未激活'})
            else:
                return render(request, 'login.html', {"msg": '用户名或密码错误'})
        else:
            return render(request, 'login.html', {"login_form":login_form})

    # def user_login(request):
    #     if request.method =="POST":
    #         user_name = request.POST.get('username', '')
    #         pass_word =request.POST.get('password', '')
    #         user = authenticate(username=user_name, password=pass_word) # 首先进行验证，If the given credentials are valid, return a User object.
    #         if user is not None:
    #             login(request, user)
    #             return render(request, 'index.html',{"username":user})
    #         else:
    #             return render(request, 'login.html',{"msg":'用户名或密码错误'})
    #     elif request.method=="GET":
    #         return render(request, "login.html",{})


class ActiveView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code =active_code)
        if all_records:
            for record in all_records:
                email= record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
        else:
            return render(request, 'active_fail.html', {})
        return render(request, 'login.html',{})  # 能够跳转，但是网址没有变化


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, "register.html", {"register_form": register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username=request.POST.get("email",'')
            password = request.POST.get('password',"")
            if UserProfile.objects.filter(email=username): # 不能用user_profile = UserProfile()，
                # user_profile.objects.filter(email=username)，因为刚新建的user不能查询
                return render(request, 'register.html', {"msg": "用户名已经存在"})
            else:
                user_profile = UserProfile()
                user_profile.email =username
                user_profile.password =make_password(password) # 加密
                user_profile.username =username
                user_profile.is_active = False
                user_profile.save()
                send_register_email(username,'register')
                # return render(request, 'login.html',{})
                return redirect('http://127.0.0.2:8000/login')  # 直接跳转到网址
        else:
            return render(request, 'register.html', {"register_form":register_form})

class ForgetpwdView(View):
    def get(self, request):
        forgetpwd_form = ForgetpwdForm()
        return render(request, 'forgetpwd.html',{"forgetpwd_form": forgetpwd_form})

    def post(self, request):
        forgetpwd_form = ForgetpwdForm(request.POST)
        if forgetpwd_form.is_valid():
            email=request.POST.get("email",'')
            if UserProfile.objects.filter(email=email):
                send_register_email(email, 'forget')
                return render(request, 'send_success.html')
            else:
                return render(request, 'forgetpwd.html', {"msg": "用户名不存在"})
        else:
            # forgetpwd_form = ForgetpwdForm()  # 如果加在前面上这一句,则每次输入栏都刷新了
            return render(request, 'forgetpwd.html',{"forgetpwd_form": forgetpwd_form})


class ResetView(View):
    def get(self, request, reset_code):
        all_records = EmailVerifyRecord.objects.filter(code=reset_code)
        if all_records:
            for record in all_records:
                email = record.email
                return render(request, "password_reset.html",{"email":email})
        else:
            return render(request, "reset_fail.html")
        return render(request, "login.html")


class ModifyPwd(View):
    def post(self, request):
        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get("password1", "")
            pwd2 = request.POST.get("password2", "")
            email= request.POST.get("email", "")
            if pwd1== pwd2:
                user_profile= UserProfile.objects.get(email=email)
                user_profile.password = make_password(pwd1)
                user_profile.save()
                return redirect("http://127.0.0.2:8000/login")
                # return render(request, "password_reset.html")
            else:
                return render(request, "password_reset.html", {"msg": '两次密码不一样'})
        else:
            return render(request, "password_reset.html", { "modify_form": modify_form})


class LogoutView(View):
    def get(self,request):
        # return redirect("/index", {"is_authenticated":False, "username": ""})
        return render(request, "index.html", {"is_authenticated": False, "username": ""})


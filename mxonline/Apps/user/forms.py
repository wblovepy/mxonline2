from django import forms
from captcha.fields import CaptchaField

class LoginForm(forms.Form):
    """采用form来进行验证，简单判断"""
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=6, max_length=12)


class RegisterForm(forms.Form):
    """ 采用form来进行验证，简单判断,同时使用验证码"""
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=6, max_length=12)
    captcha = CaptchaField(error_messages={"invalid":"验证码错误"})

class ForgetpwdForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={"invalid":"验证码错误"})

class ModifyPwdForm(forms.Form):
    password1 = forms.CharField(required=True, min_length=6, max_length=12)
    password2 = forms.CharField(required=True, min_length=6, max_length=12)
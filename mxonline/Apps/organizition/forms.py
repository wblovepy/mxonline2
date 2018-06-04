from django import forms
from operation.models import UserAsk
import re


# class UserAskForm(forms.Form):
#     name = forms.CharField(required=True, min_length=2, max_length=20)
#     phone = forms.CharField(required=True, min_length=11, max_length=11)
#     course_name = forms.CharField(required=True, min_length=2, max_length=50)


class AnotherUserForm(forms.ModelForm):
    class Meta:
        # model = UserAskForm
        model = UserAsk
        fields = ["name","mobile", "course_name"]

    def clean_mobile(self):  # 单独对字段进行验证
        """
        验证手机号码是否合法
        """
        data= self.cleaned_data
        mobile=data.get('mobile')  # 读取post表单返回的值
        REGEX_MOBILE= '^0\d{2,3}\d{7,8}$|^1[358]\d{9}$|^147\d{8}|^176\d{8}'
        p = re.compile(REGEX_MOBILE)
        if not mobile:
            if p.match(mobile):
                return data   # 必须返回data，不能只返回mobile
        else:
            raise forms.ValidationError('手机号码非法',code="mobile_invalid")





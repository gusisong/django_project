from django import forms
from django.contrib.auth.models import User


# 用户登录表单
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


# 用户注册表单
class UserRegisterForm(forms.ModelForm):
    # 复写User的密码
    password = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'email')

    # 对两次输入的密码一致性校验
    def clean_password2(self):
        data = self.cleaned_data
        if data.get('password') == data.get('password2'):
            return data.get('password')
        else:
            raise forms.ValidationError("密码输入不一致，请重试")

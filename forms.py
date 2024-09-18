from django import forms 
from .models import Photo,Your_Post,User_serach_Form
class UserName_Your1(forms.Form):
    user_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":":نام کاربی خود را وارد کنید"}))
    email = forms.EmailField(max_length=50,widget=forms.EmailInput(attrs={"placeholder":" :ایمیل خود وارد کنید"}))
    first_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={"placeholder":":نام کوچک "}))
    last_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={"placeholder":":نام خانوادگی"}))
    password_1 = forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={"placeholder":":رمز خود را وارد کنید"}))
    password_2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":":رمز خود را دوباره وارد کنید"}))
    def clean(self):
        cleaned_data = super().clean()
        password_1 = cleaned_data.get("password_1")
        password_2 = cleaned_data.get("password_2")

        if password_1 and password_2 and password_1 != password_2:
            raise forms.ValidationError("Passwords do not match.")
class Photo_Form(forms.Form):
    class Meta:
        model = Your_Post
        fields = ["image","image_2","image_3","image_4","title","text","integer"]
class User_serach_Form(forms.Form):
    class Meta:
        query = forms.CharField(label="Search", max_length=100) 
        model = User_serach_Form
        fields = ["query"]       
from django import forms
from book.models import Books
from django.contrib.auth.models import User

class BookForm(forms.Form):
    name=forms.CharField()
    author=forms.CharField()
    pages=forms.IntegerField()
    price=forms.IntegerField()



class BookModelForm(forms.ModelForm):
    class Meta:
        model=Books
        fields="__all__"

    widgets={
        
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "author":forms.TextInput(attrs={"class":"form-control"}),
            "pages":forms.NumberInput(attrs={"class":"form-control"}),
            "price":forms.NumberInput(attrs={"class":"form-control"}),




    }

class RegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","email","password"]


        widgets={
             "username":forms.TextInput(attrs={"class":"form-control"}),
             "email":forms.EmailInput(attrs={"class":"form-control"}),
             "password":forms.PasswordInput(attrs={"class":"form-control"})
                   }


class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
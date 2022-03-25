from django import forms
from django.forms import ModelForm
from .models import Fruits
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FruitAddForm(ModelForm):
    class Meta:
        model=Fruits
        fields='__all__'
        widgets={
            "fruit_name":forms.TextInput(attrs={'class':'box'}),
            "place": forms.TextInput(attrs={'class': 'box'}),
            "quantity":forms.TextInput(attrs={'class':'box'}),
            "cost":forms.TextInput(attrs={'class':'box'})
        }

    def clean(self):
        cleaned_data=super().clean()
        quantity=cleaned_data.get("quantity")
        cost=cleaned_data.get("cost")
        if quantity<0:
            msg = "invalid value. Pls provide valid value"
            self.add_error("quantity",msg)
        elif cost<0:
            msg = "invalid value. Pls provide valid value"
            self.add_error("cost", msg)

class UserRegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","first_name","last_name","email","password1","password2"]


class LoginForm(forms.Form):
    username=forms.CharField(max_length=120)
    password = forms.CharField(widget=forms.PasswordInput)

from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserCreateForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['username','first_name','password1','password2']
        
class UserAuthenticationForm(AuthenticationForm):
    class Meta:
        model = UserModel
        fields = ['username','password']
        
class AddCashForm(forms.ModelForm):
    class Meta:
        model = AddCashModel
        fields = ['source', 'amount', 'description']

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = ExpenseModel
        fields = ['description', 'amount']
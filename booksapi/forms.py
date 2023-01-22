from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import BooK


class creationUserForm(UserCreationForm):
    class meta:
        model = User
        fields = ['username' , 'email', 'password1','password2']
        
class BookForm(ModelForm):
    class Meta:
        model = BooK
        fields = '__all__'
        
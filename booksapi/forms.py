from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class creationUserForm(UserCreationForm):
    class meta:
        model = User
        fields = ['username' , 'email', 'password1','password2']
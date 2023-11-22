from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import (
    Form,
    CharField,
    PasswordInput,
)

from account.models import CustomUser


class LoginForm(Form):
    username = CharField()
    password = CharField(widget=PasswordInput)


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("age",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields

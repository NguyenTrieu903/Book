from django import forms
from django.db import models
from django.db.models import fields
from .models import ManageBook
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ManagebookForm (forms.ModelForm):
    class Meta:
        model = ManageBook
        fields = "__all__"


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')

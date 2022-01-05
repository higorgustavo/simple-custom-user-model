from django.contrib.auth import forms
from django import forms as f
from .models import Usuario, Projeto


class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = Usuario


class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = Usuario


class ProjetoForm(f.ModelForm):
    class Meta:
        model = Projeto
        fields = ['titulo', ]
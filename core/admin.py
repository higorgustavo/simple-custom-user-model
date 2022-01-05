from django import forms
from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from .models import Empresa, Projeto, Usuario
from .forms import UserChangeForm, UserCreationForm


admin.site.register(Empresa)
admin.site.register(Projeto)

@admin.register(Usuario)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = Usuario
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        ("Empresa Atuante", {"fields": ("empresa", )}),
    )

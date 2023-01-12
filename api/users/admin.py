from django.contrib import admin
from users.models import Customer
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea, CharField
from django import forms
from django.db import models


class UserAdminConfig(UserAdmin):
    model = Customer
    list_display = ('email', 'username', 'first_name',
                    'is_active', 'is_staff')

admin.site.register(Customer, UserAdminConfig)

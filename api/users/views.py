from .models import Customer
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from api.decorators import unauthenticated_user, allowed_users, admin_only
from .forms import RegistrationForm
from .models import Customer
from api.models import Post


@unauthenticated_user
def register_view(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.username = form.cleaned_data.get('username')
            user.email = form.cleaned_data.get('email')
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            login(request, user)

            messages.success(request, f"New account created: {user.username}")

            return redirect("/api/")

    context = {"register_form": form}
    return render(request=request, template_name="Register.html", context=context)

@login_required(login_url='/user/login/')
def user_profile(request):
    posts = Post.objects.filter(user=request.user)
    return render(request=request, template_name="UserProfile.html", context={'posts': posts})
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NewUserForm

# Create your views here.


def hello(request):
    return HttpResponse("Hello World")


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("main:homepage")
        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})

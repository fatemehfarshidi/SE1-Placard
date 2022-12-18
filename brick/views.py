from django.shortcuts import  render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Post
from .serializers import PostSerializer
from .forms import NewUserForm
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .decorators import unauthenticated_user

# Create your views here.

@login_required(login_url="/brick/login/")
def brick(request):
    return render(request=request, template_name="brick.html")

@unauthenticated_user
def register_request(request):
	form = NewUserForm()
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f"New account created: {username}")
			return redirect("login")
	context = {"register_form": form}
	return render(request=request, template_name="accounts/register.html", context=context)

@unauthenticated_user
def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect("/brick/")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	context = {"login_form":form}
	return render(request=request, template_name="accounts/login.html", context=context)

def logoutUser(request):
	logout(request)
	messages.success(request, "You have successfully logged out.")
	return redirect("/brick/login/")

@api_view()
def post_list(request) :
	if request.method =="GET":
		posts = Post.objects.all()
		serializer = PostSerializer(posts, many=True)
		return Response(serializer.data)
	if request.method == "POST":
		serializer = PostSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view()
def post_detail(request):
    if request.method == "GET":
        post = get_object_or_404(Post, pk=id)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    if request.method == "PUT":
        post = get_object_or_404(Post, pk=id)
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    if request.method == "DELETE":
        post = get_object_or_404(Post, pk=id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


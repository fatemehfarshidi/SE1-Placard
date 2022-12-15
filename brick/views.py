from django.shortcuts import  render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from .models import Post
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import PostSerializer



# Create your views here.
def hello(request):
    return HttpResponse("Hello world!")


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="main/register.html", context={"register_form":form})


@api_view()
def post_list(request):
    if request.method == "GET":
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
		serializer = PostSerializer(post, data = request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data)
	if request.method == "DELETE":
		post = get_object_or_404(Post, pk=id)
		post.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


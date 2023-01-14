from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import CreatePostForm
from .models import Post
from users.models import Customer

# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer

@login_required(login_url='/user/login/')
def home(request):
    posts = Post.objects.all()
    users = Customer.objects.all()

    context = {'posts': posts, 'users': users, }

    return render(request, 'Home.html', context)


@login_required(login_url='/user/login/')
def create_post(request, pk):
    user = Customer.objects.get(id=pk)
    form = CreatePostForm(initial={'user': user})
    if request.method == 'POST':
        if form.is_valid():
            post = form.save()
            post.title = form.cleaned_data.get('title')
            post.contact_info = form.cleaned_data.get('contact_info')
            post.price = form.cleaned_data.get('price')
            post.description = form.cleaned_data.get('description')
            
            post.save()
            
            messages.success(request, "Post Created successfully")
            
            return redirect("home")

    context = {'create_post_form':form}
    return render(request, 'CreatePost.html', context)

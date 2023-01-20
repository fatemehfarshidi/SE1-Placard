from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import CreatePostForm
from .models import Post
from users.models import Customer
from django.shortcuts import redirect

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

    # Get Post body
    title = request.POST.get('title')
    contact_info = request.POST.get('contact_info')
    price = request.POST.get('price')
    description = request.POST.get('description')

    if request.method == 'POST':
        Post(
            title=title,
            contact_info=contact_info,
            price=price,
            description=description,
            user=user
        ).save()
        return redirect("/api/")

    context = {'create_post_form': form}
    return render(request, 'CreatePost.html', context)


def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, "postVisibility.html", {"post": post})
    
@login_required(login_url='login')
def delete_post(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect('/api/')
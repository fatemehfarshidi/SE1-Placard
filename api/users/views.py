from .models import Customer
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import  render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from api.decorators import unauthenticated_user, allowed_users, admin_only
from .forms import RegistrationForm
from .models import Customer


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
			# group = Group.objects.get(name='customer')
			# user.groups.add(group)
            user.save()

            messages.success(request, f"New account created: {username}")
            return redirect("login")
            
    context = {"register_form": form}
    return render(request=request, template_name="account/register.html", context=context)

# class CustomUserCreate(APIView):
#     permission_classes = [AllowAny]
#     serializer_class = CustomUserSerializer

#     def get(self, request, *args, **kwargs):
#         serializer = CustomUserSerializer(Customer.objects.all(), many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request, format='json'):
#         serializer = CustomUserSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             if user:
#                 json = serializer.data
#                 return Response(json, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @unauthenticated_user
# def login(request):
# 	if request.method == "POST":
# 		form = AuthenticationForm(request, data=request.POST)
# 		if form.is_valid():
# 			username = form.cleaned_data.get('username')
# 			password = form.cleaned_data.get('password')
# 			user = authenticate(username=username, password=password)
# 			if user is not None:
# 				login(request, user)
# 				return redirect("/brick/")
# 			else:
# 				messages.error(request,"Invalid username or password.")
# 		else:
# 			messages.error(request,"Invalid username or password.")
# 	form = AuthenticationForm()
# 	context = {"login_form":form}
# 	return render(request=request, template_name="accounts/login.html", context=context)

# def logoutUser(request):
# 	logout(request)
# 	messages.success(request, "You have successfully logged out.")
# 	return redirect("/user/login/")

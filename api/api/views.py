from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .serializers import MyTokenObtainPairSerializer, RegisterSerializer, PostSerializer
from .models import Post

# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer

# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
# def testEndPoint(request):
#     if request.method == 'GET':
#         data = f"Congratulation {request.user}, your API just responded to GET request"
#         return Response({'response': data}, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         text = request.POST.get('text')
#         data = f'Congratulation your API just responded to POST request with text: {text}'
#         return Response({'response': data}, status=status.HTTP_200_OK)
#     return Response({}, status.HTTP_400_BAD_REQUEST)

##################

# class PostList(generics.ListAPIView):
#     permission_classes = [permissions.AllowAny]
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()


# class PostDetail(generics.RetrieveAPIView):
#     serializer_class = PostSerializer

#     def get_object(self, queryset=None, **kwargs):
#         item = self.kwargs.get('pk')
#         return get_object_or_404(Post, slug=item)


# class CreatePost(generics.CreateAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)


# class AuthorPostDetail(generics.RetrieveAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class EditPost(generics.UpdateAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()


# class DeletePost(generics.RetrieveDestroyAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()

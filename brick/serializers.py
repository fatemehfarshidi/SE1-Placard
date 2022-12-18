from rest_framework import serializers
from brick.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'owner', 'description', 'type', 'date_created', 'tags']

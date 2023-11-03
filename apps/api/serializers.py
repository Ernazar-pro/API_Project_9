from rest_framework.serializers import *
from apps.post.models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
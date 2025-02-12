from blockapp.models import Post
from rest_framework.serializers import ModelSerializer

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['uuid', 'title', 'content', 'created', 'updated']


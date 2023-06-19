from rest_framework import serializers
from posts.models import Posts, LikePost

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ['id', 'user', 'title', 'desc', 'image', 'created_at', 'no_of_likes']

class LikePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikePost
        fields = ['post_id', 'username', 'created_at']
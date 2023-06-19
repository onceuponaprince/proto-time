from rest_framework import viewsets
from .models import Posts, LikePost
from .serializers import PostsSerializer, LikePostSerializer
from django.shortcuts import render, redirect
from django.db.models import F

class PostsViewSet(viewsets.ModelViewSet):
    http_methods = ['get','update','post', 'delete']
    serializer_class = PostsSerializer
    
    def get_queryset(self):
        return Posts.objects.all()
    
    def perform_create(self, serializer):
        kwargs = {
            'user': self.request.user, 
            'id': self.request.id,
            'title': serializer.validated_data['title'],
            'desc': serializer.validated_data['desc'],
            'image': serializer.validated_data['image'],
            'created_at': self.request.created_at,
            'no_of_likes': serializer.validated_data['no_of_likes'],
        }
        serializer.save(**kwargs)

class LikePostViewSet(viewsets.ModelViewSet):
    http_methods = ['get','update','post', 'delete']
    serializer_class = LikePostSerializer
    
    def get_queryset(self):
        return LikePost.objects.all()
    
    def like_post(request):
        post_id = request.GET.get('post_id')

        post = Posts.objects.get(id=post_id)

        like_filter = LikePost.objects.filter(post_id=post_id)

        if like_filter == None:
            new_like = LikePost.objects.create(post_id=post_id)
            new_like.save()
            like_filter.no_of_likes += 1
            like_filter.save()
            return 
        else:
            like_filter.delete()
            post.no_of_likes = post.no_of_likes-1
            post.save()
            return redirect('/')
    
 


from rest_framework import routers

from posts.viewsets import PostsViewSet, LikePostViewSet


router = routers.SimpleRouter()
router.register(r'posts', PostsViewSet, basename='posts')
router.register(r'like_posts', LikePostViewSet, basename='like_posts')
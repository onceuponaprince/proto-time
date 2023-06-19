from django.contrib import admin

# Register your models here.
from posts.models import Posts, LikePost

admin.site.register(Posts)
admin.site.register(LikePost)
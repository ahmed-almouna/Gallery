from .models import Post
from profiles.models import Profile
from django.http import HttpResponse
from django.shortcuts import redirect

def action_permission(func):
    def wrapper(request, **kwardgs):
        pk = kwardgs.get('pk')
        profile = Profile.objects.get(user=request.user)
        post = Post.objects.get(pk=pk)
        if profile.user == post.author.user:
            print('yes')
            return func(request, **kwardgs)
        else:
            print('no')
            return redirect('posts:main-board')
        
    return wrapper
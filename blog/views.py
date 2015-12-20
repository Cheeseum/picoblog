from django.shortcuts import get_object_or_404, render

from .models import Post

def index(request):
    latest_posts_list = Post.objects.order_by('-date')[:5]
    context = {'latest_posts_list': latest_posts_list}

    return render(request, 'blog/index.html', context)

def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    return render(request, 'blog/post.html', {'post': post})

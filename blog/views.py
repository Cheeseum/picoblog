from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Post

class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_posts_list'

    def get_queryset(self):
        """Return the last five posts."""
        return Post.objects.order_by('-date')[:5]

class PostView(generic.DetailView):
    model = Post
    template_name = 'blog/post.html'

def index(request):
    latest_posts_list = Post.objects.order_by('-date')[:5]
    context = {'latest_posts_list': latest_posts_list}

    return render(request, 'blog/index.html', context)

def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    return render(request, 'blog/post.html', {'post': post})

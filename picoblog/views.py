from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Post

class IndexView(generic.ListView):
    template_name = 'picoblog/index.html'
    context_object_name = 'latest_posts_list'

    def get_queryset(self):
        """Return the last five posts."""
        return Post.objects.order_by('-date')[:5]

class PostView(generic.DetailView):
    model = Post
    template_name = 'picoblog/post.html'

def index(request):
    latest_posts_list = Post.objects.order_by('-date')[:5]
    context = {'latest_posts_list': latest_posts_list}

    return render(request, 'picoblog/index.html', context)

def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    return render(request, 'picoblog/post.html', {'post': post})

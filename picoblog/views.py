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

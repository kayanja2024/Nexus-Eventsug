from django.shortcuts import render

from .models import BlogPost


def post_list(request):
    posts = BlogPost.objects.filter(is_published=True).order_by('-published_at')
    return render(request, "blog/list.html", {"posts": posts})


# Create your views here.

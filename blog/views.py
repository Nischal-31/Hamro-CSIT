from django.shortcuts import render, get_object_or_404
from .models import Post

def blog_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/blog_list.html', {'posts': posts})

def blog_detail(request, slug):
    # Get the current post by slug
    post = get_object_or_404(Post, slug=slug)

    # Fetch the next post, you can adjust the ordering logic as per your requirements
    next_post = Post.objects.filter(created_at__gt=post.created_at).order_by('created_at').first()

    # Pass post and next_post to the template
    return render(request, 'blog/blog_detail.html', {'post': post, 'next_post': next_post})

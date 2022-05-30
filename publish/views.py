from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .models import Post
from .forms import CreatePostForm, EditPostForm

# function to list the publish news lists


def news_list(request):
    posts = Post.objects.all()
    template = "publish/publish.html"
    context = {
        "posts": posts
    }

    return render(request, template, context)

# function to render individual page of the news


def news_post(request, year, month, day, hour, minute, post):
    post = get_object_or_404(Post, slug=post, publish__year=year,
                             publish__month=month, publish__day=day,
                             publish__hour=hour, publish__minute=minute)
    template = "publish/news_post.html"
    context = {
        "post": post
    }

    return render(request, template, context)

# function to add news post only to the superuser


@user_passes_test(lambda u: u.is_superuser)
def add_post(request):
    if request.method == "POST":
        form = CreatePostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.slug = new_post.title.lower().replace(" ", "-")
            new_post = form.save()
            return render(
                request, "publish/news_post.html", {"post": new_post})
    else:
        form = CreatePostForm()
    return render(request, "publish/new_post.html", {"form": form})

# function to edit news post only to the superuser


@user_passes_test(lambda u: u.is_superuser)
def edit_post(request, year, month, day, hour, minute, post):
    post = get_object_or_404(Post, slug=post, publish__year=year,
                             publish__month=month, publish__day=day,
                             publish__hour=hour, publish__minute=minute)
    if request.method == "POST":
        form = EditPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return render(request, "publish/news_post.html", {"post": post})
    else:
        data = {"title": post.title, "body": post.body}
        form = EditPostForm(initial=data)
    return render(request, "publish/edit_post.html", {"form": form})

# function to delete news post only to the superuser


@user_passes_test(lambda u: u.is_superuser)
def delete_post(request, year, month, day, hour, minute, post):
    """
    A view to allow the super user to delete posts
    """
    post = get_object_or_404(Post, slug=post, publish__year=year,
                             publish__month=month)
    post.delete()
    return redirect(reverse("publish"))

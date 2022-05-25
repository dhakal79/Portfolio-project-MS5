from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .models import Post
from .forms import CreatePostForm, EditPostForm


def news_list(request):
    """
    A view to display the post template.
    """
    posts = Post.objects.all()

    template = "publish/publish.html"
    context = {
        "posts": posts
    }

    return render(request, template, context)


def news_post(request, year, month, post):
    """
    A view to render an individual page for each
    post in the database.
    """
    post = get_object_or_404(Post, slug=post, publish__year=year,
                             publish__month=month)
    template = "publish/news_post.html"
    context = {
        "post": post
    }

    return render(request, template, context)


@user_passes_test(lambda u: u.is_superuser)
def add_post(request):
    """
    A view to display the form allowing super
    users to create new posts
    """
    if request.method == "POST":
        form = CreatePostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.slug = new_post.title.lower().replace(" ", "-")
            new_post = form.save()
            return render(request, "publish/news_post.html", {"post": new_post})
    else:
        form = CreatePostForm()
    return render(request, "publish/new_post.html", {"form": form})


@user_passes_test(lambda u: u.is_superuser)
def edit_post(request, year, month, post):
    """
    A view to to display and submit forms to allow
    the super user to edit existing posts
    """
    post = get_object_or_404(Post, slug=post, publish__year=year,
                             publish__month=month)
    if request.method == "POST":
        form = EditPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return render(request, "publish/news_post.html", {"post": post})
    else:
        data = {"title": post.title, "body": post.body}
        form = EditPostForm(initial=data)
    return render(request, "publish/edit_post.html", {"form": form})


@user_passes_test(lambda u: u.is_superuser)
def delete_post(request, year, month, post):
    """
    A view to allow the super user to delete posts
    """
    post = get_object_or_404(Post, slug=post, publish__year=year,
                             publish__month=month)
    post.delete()
    return redirect(reverse("publish"))

from django.urls import path
from . import views

urlpatterns = [
    path("", views.news_list, name="blog"),
    path("<int:year>/<int:month>/<slug:post>/", views.blog_post, name="blog_post"),
    path("new_post/", views.add_post, name="add_post"),
    path("edit_post/<int:year>/<int:month>/<slug:post>/", views.edit_post, name="edit_post"),
    path("delete_post/<int:year>/<int:month>/<slug:post>/", views.delete_post, name="delete_post"),
]
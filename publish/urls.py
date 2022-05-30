from django.urls import path
from . import views

urlpatterns = [
    path("", views.news_list, name="publish"),
    path("<int:year>/<int:month>/<int:day>/<int:hour>/<int:minute>/<slug:post>/", views.news_post, name="news_post"),  # noqa: E501
    path("new_post/", views.add_post, name="add_post"),
    path("edit_post/<int:year>/<int:month>/<int:day>/<int:hour>/<int:minute>/<slug:post>/", views.edit_post, name="edit_post"),  # noqa: E501
    path("delete_post/<int:year>/<int:month>/<int:day>/<int:hour>/<int:minute>/<slug:post>/", views.delete_post, name="delete_post"),  # noqa: E501
]

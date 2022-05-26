from django.urls import path
from . import views

urlpatterns = [
    path("", views.view_purchase, name="view_purchase"),
    path("add/<service_id>/", views.add_to_purchase, name="add_to_purchase"),
    path("edit/<service_id>/", views.adjust_purchase, name="adjust_purchase"),
    path("remove/<service_id>/", views.remove_from_purchase, name="remove_from_purchase"),
]

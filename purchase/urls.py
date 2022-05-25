from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_purchase, name='view_purchase'),
    path('add/<item_id>/', views.add_to_purchase, name='add_to_purchase'),
    path('adjust/<item_id>/', views.adjust_purchase, name='adjust_purchase'),
    path('remove/<item_id>/', views.remove_from_purchase, name='remove_from_purchase'),
]

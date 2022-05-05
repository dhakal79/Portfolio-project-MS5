from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_purchase, name='view_purchase'),
    path('add/<item_id>/', views.add_to_purchase, name='add_to_purchase'),
]

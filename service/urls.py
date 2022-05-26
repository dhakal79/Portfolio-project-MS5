from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='service'),
    path('<int:service_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:service_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:service_id>/', views.delete_product, name='delete_product'),
]

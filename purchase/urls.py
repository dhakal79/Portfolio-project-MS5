from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_purchase, name='view_purchase')
]

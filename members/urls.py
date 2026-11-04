from django.urls import path
from . import views

urlpatterns = [
    path('', views.member_list, name='member_list'),
    path('add/', views.add_member, name='add_member'),
    path('add/verify-otp/', views.verify_add_otp, name='verify_add_otp'),
    path('edit/<int:pk>/', views.edit_member, name='edit_member'),
    path('delete/<int:pk>/', views.delete_member, name='delete_member'),
    path('delete/verify-otp/', views.verify_delete_otp, name='verify_delete_otp'),
]
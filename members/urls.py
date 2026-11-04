from django.urls import path
from . import views

urlpatterns = [
    # Landing / Home Page with Contact Form
    path('', views.home_view, name='home'),

    # Member Management Dashboard Routes
    path('members/', views.member_list, name='member_list'),
    path('members/add/', views.add_member, name='add_member'),
    path('members/add/verify-otp/', views.verify_add_otp, name='verify_add_otp'),
    path('members/edit/<int:pk>/', views.edit_member, name='edit_member'),
    path('members/delete/<int:pk>/', views.delete_member, name='delete_member'),
    path('members/delete/verify-otp/', views.verify_delete_otp, name='verify_delete_otp'),
]
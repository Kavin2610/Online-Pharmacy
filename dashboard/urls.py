from django.urls import path

from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard_view/',views.dashboard_view, name='dashboard_view'),
    path('users/', views.users, name='users'),
    path('prescriptions/', views.prescriptions, name='prescriptions'),
    path('products/',views.products, name= 'products'),
    path('new/', views.new, name='new'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('coupon/', views.coupon, name='coupon'),
    # path('add_coupon/', views.add_coupon, name="add_coupon"),
    path('create_coupon/', views.create_coupon, name='create_coupon'),
    
    path('delete-coupon/<int:pk>/', views.delete_coupon, name='delete_coupon'),
    path('delete-coupon/', views.delete_coupon, name='delete_coupon'),
    
]

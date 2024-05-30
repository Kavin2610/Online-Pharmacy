# urls.py
app_name = 'cart'

from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('cart/', views.cart, name="cart"),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart_view/', views.cart_view, name='cart_view'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.Checkout, name='checkout'),
    path('checkout/submit/', views.submit, name='submit'),
    path('checkout2/',views.cart_checkout, name="checkout2"),
    path('update_quantity/', views.update_quantity, name='update_quantity'),
    path('success/', views.success, name = "success"),
    path('cancel/', views.cancel, name = "cancel"),
    path('apply_coupon/',views.apply_coupon, name='apply_coupon'),
    path('cart_view/<int:discount>/', views.cart_view, name='cart_view'),
    path('/create-checkout-session/', views.create_checkout_session, name = "checkout" ),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('core.urls')),
    path('items/', include('item.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls')),
    path('payment/', include('payment.urls')),
    path('otp/',include('otp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)


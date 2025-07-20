from django.contrib import admin
from django.urls import path, include
from apps.products.views import ProductAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/products/', ProductAPIView.as_view())
]

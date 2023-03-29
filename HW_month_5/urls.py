
from django.contrib import admin
from django.urls import path
from product.views import product_list_category, list_Product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/api/v1/categories/', )
]
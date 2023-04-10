from django.contrib import admin
from django.urls import path, include
from Product.views import (
    ProductListCreateApiView,
    ProductRetrieveUpdateDestroyApiView
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/products/', ProductListCreateApiView.as_view()),
    path('api/v1/products/<int:id>/', ProductRetrieveUpdateDestroyApiView.as_view()),
    # path('api/v1/categories/', views.list_Category),
    # path('api/v1/categories/<int:id>/', views.list_Category_detail),
    # path('api/v1/reviews/', views.list_Review),
    # path('api/v1/reviews/<int:id>/', views.list_Review_detail),
    # path('api/v1/products/reviews/', views.products_reviews),
    path('api/v1/users/', include('users.urls'))
]

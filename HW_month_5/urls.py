from django.contrib import admin
from django.urls import path, include
from Product import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/products/', views.ProductApiView.as_view()),
    path('api/v1/products/<int:pk>/', views.ProductDetailApiView.as_view()),
    path('api/v1/categories/', views.CategoryApiView.as_view()),
    path('api/v1/categories/<int:pk>/', views.CategoryDetailApiView.as_view()),
    path('api/v1/reviews/', views.ReviewApiView.as_view()),
    path('api/v1/reviews/<int:pk>/', views.ReviewDetailApiView.as_view()),
    path('api/v1/products/reviews/', views.ProductReviewApiView.as_view()),
    path('api/v1/users/', include('users.urls'))
]

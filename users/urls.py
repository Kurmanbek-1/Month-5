from django.urls import path
from . import views

urlpatterns = [
    path('authorization/', views.AuthorizationApiView.as_view()),
    path('registration/', views.RegistrationApiView.as_view()),
    path('api/v1/users/confirm/', views.UserCreateAPIView.as_view())
]

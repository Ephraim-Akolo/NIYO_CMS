from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.CreateUserView.as_view()),
    path('token/', views.TokenObtainPairView.as_view()),
    path('token/refresh/', views.TokenRefreshView.as_view()),
]
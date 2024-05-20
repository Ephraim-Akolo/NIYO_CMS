from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListCreateTaskView.as_view()),
    path('<uuid:pk>/', views.RetrieveUpdateDestroyTaskView.as_view())
]
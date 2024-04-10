from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_application, name='job_application'),
    path('result/<int:pk>/', views.result, name='result'),
]

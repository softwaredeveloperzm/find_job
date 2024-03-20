from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('job_listing', views.job_listing, name='job_listing'),
    path('job_details/<int:pk>/', views.job_details, name='job_details')
]
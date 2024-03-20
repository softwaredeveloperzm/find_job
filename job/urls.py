from django.urls import path
from . import views

urlpatterns = [
    path('create_job/', views.create_job, name='create_job'),
    path('manage_job', views.manage_job, name='manage_job'),
    path('apply_to_job/<int:pk>/', views.apply_to_job, name='apply_to_job'),
    path('all_applicants/<int:pk>/', views.all_applicants, name='all_applicants'),
    path('applied_jobs/', views.applied_jobs, name='applied_jobs'),
  
]
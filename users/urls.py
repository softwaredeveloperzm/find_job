from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.login_user, name='login'),
    path('register-applicant/', views.register_applicant, name='register_applicant'),
    path('register-recruiter/', views.register_recruiter, name='register_recruiter'),
    path('logout/', views.logout_user, name='logout'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="users/password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_confrim.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"), name="password_reset_complete"),
]   
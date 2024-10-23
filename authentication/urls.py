from django.urls import path
from .views import RegisterView, LoginView, logout_view, ForgotPasswordView, ResetPasswordView, login_page, register_page , dashboard

urlpatterns = [
    path('v1/register/', RegisterView.as_view(), name='register'),
    path('v1/login/', LoginView.as_view(), name='login'),
    path('v1/logout/', logout_view , name='logout'),
    path('v1/forgot-password/', ForgotPasswordView.as_view(), name='forgot_password'),
    path('v1/reset-password/', ResetPasswordView.as_view(), name='reset_password'),
    path('login/', login_page, name='login_page'),
    path('register/', register_page, name='register_page'),
    path('dashboard/', dashboard, name='dashboard'),
]

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework import status
from .models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from rest_framework_simplejwt.tokens import RefreshToken
import secrets
from django.contrib.auth.hashers import make_password
from .serializers import UserSerializer
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password
from .serializers import UserSerializer  # Make sure your serializer is correctly imported

class RegisterView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()  
            user.password = make_password(serializer.validated_data['password'])  
            user.save()
            
            return redirect("login_page")
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return render(request, 'authentication/login.html')

    def post(self, request):
        username = request.POST.get('username')  
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
            print("User found in DB: ", user)
        except User.DoesNotExist:
            user = None
            print("User does not exist in DB.")
        
        if user is not None:
            user = authenticate(request, username=username, password=password)
            print("Here is the authenticated user: ", user)
            if user is not None:
                login(request, user)
      
                refresh = RefreshToken.for_user(user)
                
                response = redirect('dashboard')
                response.set_cookie(key='access_token', value=str(refresh.access_token), httponly=True)
                response.set_cookie(key='refresh_token', value=str(refresh), httponly=True)
                
                return response
            else:
                print("Authentication failed.")
                return render(request, 'authentication/login.html', {'error': 'Invalid credentials'})
        else:
            return render(request, 'authentication/login.html', {'error': 'User does not exist'})


def logout_view(request):
    logout(request)
    return redirect('login_page')


class ForgotPasswordView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        try:
            user = User.objects.get(email=email)
            reset_token = secrets.token_urlsafe(32)
            user.reset_password_token = reset_token
            user.save()

            send_mail(
                'Password Reset Request',
                f'Use the following token to reset your password: {reset_token}',
                'your-email@example.com',
                [email],
                fail_silently=False,
            )
            return Response({"message": "Password reset email sent"}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "User does not exist"}, status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        token = request.data.get('token')
        new_password = request.data.get('new_password')

        try:
            user = User.objects.get(reset_password_token=token)
            user.set_password(new_password)
            user.reset_password_token = None
            user.save()
            return Response({"message": "Password reset successful"}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)


def custom_login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login_page')
        return view_func(request, *args, **kwargs)
    return wrapper


@custom_login_required
def dashboard(request):
    user = request.user
    return render(request, 'dashboard.html', {'user': user})


def login_page(request):
    return render(request, 'authentication/login.html')


def register_page(request):
    return render(request, 'authentication/register.html')

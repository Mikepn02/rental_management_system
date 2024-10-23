from django.contrib import admin
from django.urls import path , include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),
    path('api/', include('rental.urls')),
    path('api/', include('tenant.urls')),
    path('api/', include('lease_agreements.urls'))
]

from django.urls import path
from .views import (
    create_tenant_view,
    tenant_list_view,
    update_tenant_view,
    delete_tenant_view
)


urlpatterns = [
    path('tenants', tenant_list_view , name='tenant_list'),
    path('v1/tenants/create/', create_tenant_view, name='create_tenant'),
    path('v1/tenants/update/<int:pk>/', update_tenant_view, name='update_tenant'),
    path('v1/tenants/delete/<int:pk>/', delete_tenant_view, name='delete_tenant'),
]
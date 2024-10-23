from django.urls import path
from .views import (
    lease_agreement_list_view,
    create_lease_agreement_view,
    update_lease_agreement_view,
    delete_lease_agreement_view
    
)

urlpatterns = [
    path('agreements/', lease_agreement_list_view, name="lease_agreement_list"),  
    path('v1/agreements/create/', create_lease_agreement_view, name='create_lease_agreement'),
    path('v1/agreements/update/<int:pk>/',update_lease_agreement_view, name='update_lease_agreement'),
    path('v1/agreements/delete/<int:pk>/', delete_lease_agreement_view, name='delete_lease_agreement'),
]

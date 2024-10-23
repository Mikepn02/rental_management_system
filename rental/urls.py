from django.urls import path
from .views import (
    rental_properties_page,
    update_property_view,
    create_property_view,
    delete_property_view
)

urlpatterns = [
    path('properties/', rental_properties_page, name="rental_properties"),  
    path('v1/properties/create/', create_property_view, name='create_property'),
    path('v1/properties/update/<int:pk>/', update_property_view, name='update_property'),
    path('v1/properties/delete/<int:pk>/', delete_property_view, name='delete_property'),
]

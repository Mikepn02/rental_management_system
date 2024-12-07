import os
import django
from faker import Faker
from random import choice, uniform
from decimal import Decimal

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rental_management.settings")
django.setup()

from rental.models import Property
from tenant.models import Tenant

fake = Faker()

def generate_and_save_properties(n=5, print_records=False):
    """Generate and save n Property records."""
    property_types = ['House', 'Apartment']
    statuses = ['available', 'rented', 'pending']
    properties = []

    for _ in range(n):
        property_data = Property(
            property_name=fake.street_name(),
            address=fake.address(),
            owner=fake.name(),
            property_type=choice(property_types),
            rent_amount=round(Decimal(uniform(500, 5000)), 2),
            monthly_expenses=round(Decimal(uniform(50, 1000)), 2),
            status=choice(statuses),
        )
        properties.append(property_data)

        if print_records:  
            print({
                "property_name": property_data.property_name,
                "address": property_data.address,
                "owner": property_data.owner,
                "property_type": property_data.property_type,
                "rent_amount": property_data.rent_amount,
                "monthly_expenses": property_data.monthly_expenses,
                "status": property_data.status,
            })

    Property.objects.bulk_create(properties, batch_size=1000)
    print(f"{n} Property records saved to the database.")

def generate_and_save_tenants(n=5, print_records=False):
    """Generate and save Tenant records."""
    tenants = []

    for _ in range(n):
        phone_number = fake.phone_number()
        if len(phone_number) > 15:
            phone_number = phone_number[:15]

        tenants.append(Tenant(
            name=fake.name(),
            email=fake.email(),
            phone_number=phone_number,
        ))

        if print_records:
            print({
                "name": tenants[-1].name,
                "email": tenants[-1].email,
                "phone_number": tenants[-1].phone_number,
            })

    Tenant.objects.bulk_create(tenants, batch_size=1000)
    print(f"Generated and saved {n} Tenant records.")

def print_saved_properties():
    """Retrieve and print saved Property records from the database."""
    properties = Property.objects.all()[:5] 
    print("\nSaved Property Records:")
    for prop in properties:
        print({
            "property_name": prop.property_name,
            "address": prop.address,
            "owner": prop.owner,
            "property_type": prop.property_type,
            "rent_amount": prop.rent_amount,
            "monthly_expenses": prop.monthly_expenses,
            "status": prop.status,
            "created_at": prop.created_at,
        })

def print_saved_tenants():
    """Retrieve and print saved Tenant records from the database."""
    tenants = Tenant.objects.all()[:5]  
    print("\nSaved Tenant Records:")
    for tenant in tenants:
        print({
            "name": tenant.name,
            "email": tenant.email,
            "phone_number": tenant.phone_number,
        })

if __name__ == "__main__":
    print("Generating and saving 500,000 Property records...")
    generate_and_save_properties(500000, print_records=False)

    print("Generating and saving 500,000 Tenant records...")
    generate_and_save_tenants(500000, print_records=False)
    print_saved_properties()
    print_saved_tenants()

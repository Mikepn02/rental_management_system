from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PropertyForm
from .models import Property
from authentication.models import User
import logging
from django.core.paginator import Paginator
import json
from django.http import JsonResponse
from django.core.serializers import serialize
from django.http import JsonResponse
import json

logger = logging.getLogger(__name__)

def rental_properties_page(request):
    logger.debug(f"User is authenticated: {request.user.is_authenticated}")
    logger.debug(f"User: {request.user}")

    if not request.user.is_authenticated:
        return redirect('login_page')

    user = request.user
    
    properties = Property.objects.all().order_by('-created_at')
    serialized_properties = serialize('json', properties)
    parsed_properties = json.loads(serialized_properties)
    
    

    paginator=Paginator(properties,10)
    page_number=request.GET.get('page',1)
    proterties_page=paginator.get_page(page_number)
    return render(request, 'properties/properties.html', {'properties': proterties_page, 'user': user})
    # return JsonResponse({"properties": parsed_properties}, safe=False)





@login_required
def create_property_view(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rental_properties')
    else:
        form = PropertyForm()

    return render(request, 'properties/property_form.html', {'form': form})


@login_required
def update_property_view(request, pk):
    property_instance = get_object_or_404(Property, pk=pk)
    
    if request.method == 'POST':
        form = PropertyForm(request.POST, instance=property_instance)
        if form.is_valid():
            form.save()
            return redirect('rental_properties')
    else:
        form = PropertyForm(instance=property_instance)

    return render(request, 'properties/property_form.html', {'form': form})


@login_required
def delete_property_view(request, pk):
    property_instance = get_object_or_404(Property, pk=pk)
    if request.method == 'POST':
        property_instance.delete()
        return redirect('rental_properties')

    return render(request, 'properties/property_confirm_delete.html', {'property': property_instance})

from django.shortcuts import get_object_or_404 , redirect , render
from .forms import TenantForm
from .models import Tenant
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

@login_required
def tenant_list_view(request):
    tenants = Tenant.objects.all()
    paginator = Paginator(tenants , 10)
    page_number = request.GET.get('page', 1)
    tenants_page = paginator.get_page(page_number)
    return render(request , 'tenants/tenant_list.html', {'tenants': tenants_page})


@login_required
def create_tenant_view(request):
    if request.method == 'POST' :
        form = TenantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tenant_list')
    
    else:
        form = TenantForm()
    return render(request ,'tenants/tenant_form.html', {'form' : form})


@login_required
def update_tenant_view(request, pk):
    tenant_instance = get_object_or_404(Tenant, pk=pk)
    
    if request.method == 'POST':
        form = TenantForm(request.POST, instance=tenant_instance)
        if form.is_valid():
            form.save()
            return redirect('tenant_list')
    else:
        form = TenantForm(instance=tenant_instance)

    return render(request, 'tenants/tenant_form.html', {'form': form})




@login_required
def delete_tenant_view(request , pk):
    tenant_instance = get_object_or_404(Tenant , pk=pk)
    if request.method == 'POST':
        tenant_instance.delete()
        return redirect('tenant_list')
    
    return render(request , 'tenants/tenant_confirm_delete.html', {'tenant': tenant_instance})

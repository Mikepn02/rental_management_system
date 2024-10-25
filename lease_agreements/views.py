from django.shortcuts import get_object_or_404, render, redirect
from .forms import LeaseAgreementForm
from .models import LeaseAgreement
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

@login_required
def lease_agreement_list_view(request):
    lease_agreements = LeaseAgreement.objects.all()
    paginator = Paginator(lease_agreements , 10)
    page_number = request.GET.get('page', 1)
    lease_agreements_page = paginator.get_page(page_number)
    return render(request, 'leases/lease_agreement_list.html', {'lease_agreements': lease_agreements_page})


@login_required
def create_lease_agreement_view(request):
    if request.method == 'POST':
        form = LeaseAgreementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lease_agreement_list')
    else:
        form = LeaseAgreementForm()

    return render(request, 'leases/lease_agreement_form.html', {'form': form})


@login_required
def update_lease_agreement_view(request, pk):
    lease_instance = get_object_or_404(LeaseAgreement, pk=pk)
    
    if request.method == 'POST':
        form = LeaseAgreementForm(request.POST, instance=lease_instance)
        if form.is_valid():
            form.save()
            return redirect('lease_agreement_list')
    else:
        form = LeaseAgreementForm(instance=lease_instance)

    return render(request, 'leases/lease_agreement_form.html', {'form': form})


@login_required
def delete_lease_agreement_view(request, pk):
    lease_instance = get_object_or_404(LeaseAgreement, pk=pk)
    if request.method == 'POST':
        lease_instance.delete()
        return redirect('lease_agreement_list')

    return render(request, 'leases/lease_agreement_confirm_delete.html', {'lease_agreement': lease_instance})

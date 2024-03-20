from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Company
from users.models import User
from .form import UpdateCompanyForm
from django.shortcuts import get_object_or_404


def update_company(request):
    try:
        company = Company.objects.get(user=request.user)
        created = False
    except Company.DoesNotExist:
        company = None
        created = True

    if request.method == 'POST':
        form = UpdateCompanyForm(request.POST, instance=company)
        if form.is_valid():
            company = form.save(commit=False)
            company.user = request.user  # Associate the current user with the company
            company.save()
            request.user.has_company = True
            request.user.save()
            messages.info(request, 'Your company information has been updated.')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong. Please check your input.')
    else:
        form = UpdateCompanyForm(instance=company)

    context = {'form': form, 'created': created}
    return render(request, 'company/update_company.html', context)


    

#view company details

def company_details(request, pk):
    company = Company.objects.get(pk=pk)
    context = {'company': company}
    return render(request, 'company/company_details.html', context)


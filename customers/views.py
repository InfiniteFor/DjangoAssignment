from django.shortcuts import render
from .forms import CustomerForm
from .models import Customer
 
def customerform(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            form.FirstName = form.cleaned_data['FirstName']
            return render(request, 'results.html', {
            'FirstName': form.cleaned_data['FirstName']})
    else:        
        form = CustomerForm()
    return render(request, 'form.html', {'form':form,'Title':'Customers'})
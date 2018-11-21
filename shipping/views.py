from django.shortcuts import render
from .forms import ShippingForm
from .models import Details
 
def shippingform(request):
    if request.method == 'POST':
        form = ShippingForm(request.POST)
        if form.is_valid():
            form.save()
            form.FirstName = form.cleaned_data['FirstName']
            return render(request, 'results.html', {
            'FirstName': form.cleaned_data['FirstName']})
    else:        
        form = ShippingForm()
    return render(request, 'form.html', {'form':form,'Title':'Shipping'})
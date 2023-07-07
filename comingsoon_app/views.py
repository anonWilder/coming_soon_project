from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Subscription

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Subscription

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if not Subscription.objects.filter(email=email).exists():
            Subscription.objects.create(email=email)
        return HttpResponseRedirect(request.path_info)  # Redirect back to the same page
    return render(request, 'coming.html')  # Render the coming.html template for GET requests


from django.shortcuts import render

def coming_soon(request):
    # Your view logic here
    return render(request, 'coming.html')

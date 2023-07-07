from django.shortcuts import render, redirect
from subscription.models import Subscriber

from django.contrib import messages

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('E-mail')
        subscriber = Subscriber(email=email)
        subscriber.save()
        messages.success(request, 'Thank you for subscribing!')
    return render(request, 'coming.html')

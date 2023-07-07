from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Subscription

admin.site.register(Subscription)

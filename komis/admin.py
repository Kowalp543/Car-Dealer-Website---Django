from django.contrib import admin

# Register your models here.
from .models import Samochod
from .models import Kupujacy

admin.site.register(Samochod)
# admin.site.register(Kupujacy)



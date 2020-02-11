from django.contrib import admin
from .models import ContactUs, MovieManagerPage

# Register your models here.

admin.site.register([ContactUs, MovieManagerPage])
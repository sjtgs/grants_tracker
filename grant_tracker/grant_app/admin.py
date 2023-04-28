from django.contrib import admin
from .models import Category, Priority, Grant_Management

# Register your models here.
admin.site.register(Category)
admin.site.register(Priority)
admin.site.register(Grant_Management)

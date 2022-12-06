from django.contrib import admin

# Register your models here.
from .models import Category,Sub_Category

admin.site.register(Category)
admin.site.register(Sub_Category)

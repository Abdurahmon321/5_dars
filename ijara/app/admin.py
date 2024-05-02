from django.contrib import admin

# Register your models here.
from .models import Home, Category

admin.site.register(Home)
admin.site.register(Category)

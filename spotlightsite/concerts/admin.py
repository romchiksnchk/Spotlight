from django.contrib import admin
from .models import Concert
from .models import Category
# Register your models here.


admin.site.register(Concert)
admin.site.register(Category)
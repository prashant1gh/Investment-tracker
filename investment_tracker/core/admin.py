from django.contrib import admin
from .models import Investment, Product, Expense

admin.site.register(Investment)
admin.site.register(Product)
admin.site.register(Expense)

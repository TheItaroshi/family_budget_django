from django.contrib import admin
from .models import Budget, BudgetElement


# Register your models here.
admin.site.register(Budget)
admin.site.register(BudgetElement)

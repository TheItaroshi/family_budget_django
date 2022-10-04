from django.shortcuts import render
from .models import Budget


# Create your views here.
def index(request):
    budgets = Budget.objects.all()
    return render(request, 'family_budget_base.html', {'budget_list': budgets})

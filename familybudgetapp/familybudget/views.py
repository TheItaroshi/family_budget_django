from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .models import Budget


# Create your views here.
def index(request):
    budgets = Budget.objects.all()
    return render(request, 'family_budget_base.html', {'budget_list': budgets})


@require_http_methods(['POST'])
def add(request):
    title = request.POST['title']
    amount_of_budget = request.POST['amount_of_budget']
    budget = Budget(title=title, amount_of_budget=amount_of_budget)
    budget.save()
    return redirect('index')


def add_to_budget(request, budget_id):
    budget = Budget.objects.get(id=budget_id)
    budget.amount_of_budget += int(request.POST['add_to_budget'])
    budget.save()
    return redirect('index')


def take_from_budget(request, budget_id):
    budget = Budget.objects.get(id=budget_id)
    budget.amount_of_budget -= int(request.POST['take_from_budget'])
    budget.save()
    return redirect('index')


def delete(request, budget_id):
    budget = Budget.objects.get(id=budget_id)
    budget.delete()
    return redirect('index')

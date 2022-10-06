from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .models import Budget, BudgetElement


# Create your views here.
def index(request):
    budgets = Budget.objects.all()
    budget_elems = BudgetElement.objects.all()
    print(budget_elems)
    return render(request, 'family_budget_base.html', {'budget_list': budgets,
                                                       'budget_element_list': budget_elems})


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


def add_element_to_budget(request, budget_id):
    budget = Budget.objects.get(id=budget_id)
    description_of_element = request.POST['description_of_element']
    value_of_element = request.POST['value_of_element']
    budget_element = BudgetElement(budget=budget, description_of_element=description_of_element,
                                   value_of_element=value_of_element)
    budget.amount_of_budget -= int(value_of_element)
    budget_element.save()
    budget.save()
    return redirect('index')


def delete_element_from_budget(request, element_id):
    budget_element = BudgetElement.objects.get(id=element_id)
    budget = budget_element.budget
    budget.amount_of_budget += budget_element.value_of_element
    budget.save()
    budget_element.delete()
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

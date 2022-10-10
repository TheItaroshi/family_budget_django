from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import FormView

from .models import Budget, BudgetElement
from .filter import BudgetFilter


class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')


class CustomRegisterView(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(CustomRegisterView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('index')
        return super(CustomRegisterView, self).get(*args, **kwargs)


@login_required(login_url='login')
def index(request):
    queryset = Budget.objects.all()
    filterset = BudgetFilter(data=request.GET, queryset=queryset)
    budgets = filterset.qs
    budget_elems = BudgetElement.objects.all()
    print(budgets)
    print(queryset)
    return render(request, 'family_budget_base.html', {
        'filter': filterset,
        'budget_list': budgets,
        'budget_element_list': budget_elems})


@require_http_methods(['POST'])
def add(request):
    user = request.user
    title = request.POST['title']
    amount_of_budget = request.POST['amount_of_budget']
    category = request.POST['category']
    group = request.POST['group']
    budget = Budget(user=user, title=title, amount_of_budget=amount_of_budget, category=category, group=group)
    budget.save()
    return redirect('index')


def add_to_budget(request, budget_id):
    budget = Budget.objects.get(id=budget_id)
    budget.amount_of_budget += int(request.POST['add_to_budget'])
    budget.save()
    return redirect('index')


def add_element_to_budget(request, budget_id):
    user = request.user
    budget = Budget.objects.get(id=budget_id)
    description_of_element = request.POST['description_of_element']
    value_of_element = request.POST['value_of_element']
    budget_element = BudgetElement(user=user, budget=budget, description_of_element=description_of_element,
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

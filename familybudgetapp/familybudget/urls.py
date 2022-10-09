from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import index, add, delete, add_to_budget, take_from_budget, add_element_to_budget, \
    delete_element_from_budget, CustomLoginView, CustomRegisterView

urlpatterns = [
    path('', index, name='index'),
    path('add', add, name='add'),
    path('delete/<int:budget_id>/', delete, name='delete'),
    path('add_to_budget/<int:budget_id>/', add_to_budget, name='add_to_budget'),
    path('take_from_budget/<int:budget_id>/', take_from_budget, name='take_from_budget'),
    path('add_element_to_budget/<int:budget_id>/', add_element_to_budget, name='add_element_to_budget'),
    path('delete_element_from_budget/<int:element_id>/', delete_element_from_budget, name='delete_element_from_budget'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', CustomRegisterView.as_view(), name='register')
]

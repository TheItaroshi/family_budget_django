from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('delete/<int:budget_id>/', views.delete, name='delete'),
    path('add_to_budget/<int:budget_id>/', views.add_to_budget, name='add_to_budget'),
    path('take_from_budget/<int:budget_id>/', views.take_from_budget, name='take_from_budget')
]

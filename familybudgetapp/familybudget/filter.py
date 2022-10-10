import django_filters
from .models import Budget


class BudgetFilter(django_filters.FilterSet):

    class Meta:
        model = Budget
        fields = {
            'title': ['contains'],
            'complete': ['exact'],
            'category': ['exact'],
            'group': ['exact']
        }

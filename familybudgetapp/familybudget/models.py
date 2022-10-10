from django.db import models
from django.contrib.auth.models import User


CATEGORIES = (
    ('food', 'Food'),
    ('utilities', 'Utilities'),
    ('clothing', 'Clothing'),
    ('transport', 'Transport'),
    ('payments', 'Payments'),
    ('uncategorized', 'Uncategorized')
)

GROUPS = (
    ('private', 'Private'),
    ('family', 'Family')
)


class Budget(models.Model):
    user = models.ForeignKey(User, models.CASCADE, null=False, blank=False)
    title = models.CharField(max_length=100, null=False, blank=False)
    amount_of_budget = models.IntegerField(null=False, blank=False)
    complete = models.BooleanField(default=False)
    category = models.CharField(max_length=20, choices=CATEGORIES, default='uncategorized')
    group = models.CharField(max_length=20, choices=GROUPS, default='private')

    def __str__(self):
        return self.title


class BudgetElement(models.Model):
    user = models.ForeignKey(User, models.CASCADE, null=False, blank=False)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, null=False, blank=False)
    description_of_element = models.CharField(max_length=250, null=False, blank=False)
    value_of_element = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.description_of_element

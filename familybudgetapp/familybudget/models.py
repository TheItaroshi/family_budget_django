from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Budget(models.Model):
    user = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=100, null=False, blank=False)
    amount_of_budget = models.IntegerField()
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class BudgetElement(models.Model):
    user = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, null=False, blank=False)
    description_of_element = models.CharField(max_length=250, null=False, blank=False)
    value_of_element = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.description_of_element

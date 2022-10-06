from django.db import models


# Create your models here.
class Budget(models.Model):
    title = models.CharField(max_length=100)
    amount_of_budget = models.IntegerField()
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class BudgetElement(models.Model):
    budget = models.ForeignKey(Budget, models.CASCADE)
    description_of_element = models.CharField(max_length=250)
    value_of_element = models.IntegerField()

    def __str__(self):
        return self.description_of_element

from django.db import models


# Create your models here.
class Budget(models.Model):
    title = models.CharField(max_length=100)
    amount_of_budget = models.IntegerField()
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title

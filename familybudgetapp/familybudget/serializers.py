from rest_framework import serializers
from .models import Budget, BudgetElement


class BudgetSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Budget
        fields = [
            'id',
            'user',
            'title',
            'amount_of_budget',
            'complete',
            'category',
            'group'
        ]


class BudgetElementSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = BudgetElement
        fields = [
            'id',
            'user',
            'budget',
            'description_of_element',
            'value_of_element'
        ]
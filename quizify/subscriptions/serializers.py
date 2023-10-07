from rest_framework import serializers
from subscriptions.models import Plan, Payment
from accounts.serializers import UserSerializer


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ['name']


class PaymentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    plan = PlanSerializer(read_only=True)

    class Meta:
        model = Payment
        fields = '__all__'

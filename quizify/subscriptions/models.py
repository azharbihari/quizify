import time
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()


class Plan(models.Model):
    name = models.CharField(max_length=100)
    months = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Subscription(models.Model):
    SUBSCRIPTION_STATUS = [
        ("active", "Active"),
        ("inactive", "Inactive"),
        ("expired", "Expired"),
        ("canceled", "Canceled"),
    ]

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="subscription")
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)

    status = models.CharField(
        max_length=20, choices=SUBSCRIPTION_STATUS, default='inactive')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.first_name}'s Subscription"


class Payment(models.Model):

    PAYMENT_STATUS = [
        ("created", "Created"),
        ("attempted", "Attempted"),
        ("paid", "Paid"),
    ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="payments")
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    razorpay_order_id = models.CharField(max_length=100)
    razorpay_payment_id = models.CharField(max_length=100)
    razorpay_signature = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20, choices=PAYMENT_STATUS, default='created')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Payment of {self.plan.price} for {self.plan.name} plan"

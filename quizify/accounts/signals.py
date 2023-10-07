# from django.db import models
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.contrib.auth import get_user_model
# from subscriptions.models import Plan, Subscription, Payment

# User = get_user_model()


# @receiver(post_save, sender=User)
# def create_subscription(sender, instance, created, **kwargs):
#     if created:
#         plan = Plan.objects.get(name="Basic")
#         Subscription.objects.create(user=instance, plan=plan, status="active")

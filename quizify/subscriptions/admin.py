from django.contrib import admin
from subscriptions.models import Subscription, Plan, Payment

admin.site.register(Plan)
admin.site.register(Subscription)
admin.site.register(Payment)

from django.contrib import admin
from django.urls import path, include
from subscriptions.views import SubscriptionCreateView, PaymentUpdateView
urlpatterns = [
    path('', SubscriptionCreateView.as_view(), name='subscription-create'),
    path('payment/', PaymentUpdateView.as_view(),
         name='payment-update'),
]

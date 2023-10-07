import time
from django.contrib.auth.models import User
import razorpay
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from subscriptions.models import Plan, Subscription, Payment
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from subscriptions.serializers import PlanSerializer, PaymentSerializer
from rest_framework.permissions import IsAuthenticated

client = razorpay.Client(
    auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

client.set_app_details({"title": "Attempter", "version": "1.0"})


class SubscriptionCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            serializer = PlanSerializer(data=request.data)
            if serializer.is_valid():
                plan = Plan.objects.get(name=serializer.validated_data['name'])

                user = request.user

                if user.has_active_subscription:
                    return Response({'message': 'You already have an active subscription'}, status=status.HTTP_400_BAD_REQUEST)

                last_unsuccessful_payment = Payment.objects.filter(
                    user=request.user,
                    plan=plan,
                    status='created',
                ).order_by('-created_at').first()

                if last_unsuccessful_payment:
                    serializer = PaymentSerializer(last_unsuccessful_payment)
                    return Response(serializer.data, status=status.HTTP_201_CREATED)

                order = client.order.create(data={
                    'amount': int(plan.price * 100),
                    'currency': 'INR',
                    'receipt': f'order_{int(time.time())}',
                })

                payment = Payment.objects.create(
                    user=user,
                    plan=plan,
                    status=order['status'],
                    razorpay_order_id=order['id'],
                )
                serializer = PaymentSerializer(payment)
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Plan.DoesNotExist:
            return Response({'error': 'Plan not found'}, status=status.HTTP_400_BAD_REQUEST)

        except Subscription.DoesNotExist:
            return Response({'error': 'Subscription not found'}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'error': 'An error occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PaymentUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            serializer = PaymentSerializer(data=request.data)
            print(request.data)
            if serializer.is_valid():
                payment = Payment.objects.get(
                    razorpay_order_id=serializer.validated_data['razorpay_order_id'])
                verified = client.utility.verify_payment_signature(
                    {
                        'razorpay_signature': serializer.validated_data['razorpay_signature'],
                        'razorpay_payment_id': serializer.validated_data['razorpay_payment_id'],
                        'razorpay_order_id': payment.razorpay_order_id
                    }
                )

                if verified:
                    payment.status = 'paid'
                    payment.razorpay_payment_id = serializer.validated_data['razorpay_payment_id']
                    payment.razorpay_signature = serializer.validated_data['razorpay_signature']
                    payment.save()

                    subscription = payment.user.subscription
                    subscription.status = 'active'
                    subscription.plan = payment.plan
                    subscription.save()

                    return Response(status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'Payment verification failed'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Payment.DoesNotExist:
            return Response({'error': 'Payment not found'}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(e)
            return Response({'error': 'An error occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

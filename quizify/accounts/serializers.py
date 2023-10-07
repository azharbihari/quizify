from rest_framework import serializers

from subscriptions.models import Subscription

from django.contrib.auth import get_user_model

User = get_user_model()


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    has_active_subscription = serializers.BooleanField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name',
                  'last_name', 'password', 'has_active_subscription')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class TokenPairSerializer(serializers.Serializer):
    access_token = serializers.CharField()
    refresh_token = serializers.CharField()


class TokenRefreshSerializer(serializers.Serializer):
    refresh = serializers.CharField()

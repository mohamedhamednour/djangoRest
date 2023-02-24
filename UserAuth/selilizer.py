from django.contrib.auth.models import User
from rest_framework import serializers


class USer_register(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password',
                  'email', 'first_name', 'last_name')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

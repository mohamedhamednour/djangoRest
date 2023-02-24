from rest_framework import serializers
from .models import Product, OrderItem, Cart
from django.contrib.auth.models import User

#hide importn
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User()
        exclude = ['password', 'last_login', 'is_superuser', 'is_staff',
                   'date_joined', 'groups', 'user_permissions']


class Products(serializers.ModelSerializer):
    admin = UserSerializer(read_only=True)

    def to_internal_value(self, data):
        self.fields['admin'] = serializers.PrimaryKeyRelatedField(
            queryset=User.objects.all())
        return super(Products, self).to_internal_value(data)
    class Meta:
        model = Product
        fields = '__all__'


class order(serializers.ModelSerializer):
    order_user = UserSerializer(read_only=True)

    def to_internal_value(self, data):
        self.fields['order_user'] = serializers.PrimaryKeyRelatedField(
            queryset=User.objects.all())
        return super(order, self).to_internal_value(data)

    class Meta:
        model = OrderItem
        fields = '__all__'


class cart(serializers.ModelSerializer):

    order_user = UserSerializer(read_only=True)

    def to_internal_value(self, data):
        self.fields['order_user'] = serializers.PrimaryKeyRelatedField(
            queryset=User.objects.all())
        return super(cart, self).to_internal_value(data)
    class Meta:
        model = Cart
        fields = '__all__'




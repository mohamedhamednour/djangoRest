from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .selilizer import USer_register
from rest_framework import generics

#register
class register(generics.ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = USer_register

#login bu token

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        serializer = USer_register(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
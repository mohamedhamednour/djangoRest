from django.urls import path
from UserAuth import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('register/', views.register.as_view()),
    path('login/', views.MyTokenObtainPairView.as_view(), name='apitest'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),]
# urls.py
from django.urls import path
from .views import UserAPIView

urlpatterns = [
    path('user/', UserAPIView.as_view(), name='user-api'),
]

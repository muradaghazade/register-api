from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from accounts.models import User
from .serializers import UserRegisterSerializer

class RegisterUserAPI(CreateAPIView):
    model = User
    serializer_class = UserRegisterSerializer

class ShowUsersAPI(ListAPIView):
    model = User
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()
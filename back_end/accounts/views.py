from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer,CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class UserSignup(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
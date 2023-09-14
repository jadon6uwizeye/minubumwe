from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer

class UserSignup(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
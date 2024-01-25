from .models import User
from .serializers import PortfolioUserSerializer
from djoser.views import UserViewSet, TokenDestroyView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class PortfolioUserViewSet(UserViewSet):
    queryset = User.objects.all()
    serializer_class = PortfolioUserSerializer

class PortfolioTokenDestroyView(TokenDestroyView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        """
        Override the post method to handle token destruction.
        """
        # Call the parent class method to destroy the token
        response = super().post(request, *args, **kwargs)

        # Add custom logic if needed

        return response
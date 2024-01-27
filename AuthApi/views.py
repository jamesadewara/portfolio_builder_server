from .models import User
from .serializers import PortfolioUserSerializer
from djoser.views import UserViewSet, TokenDestroyView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import get_user_model


User = get_user_model()

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
    
class PortfolioUserDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        user_id = request.user.id

        try:
            user = User.objects.get(pk=user_id)
            user.delete()
            return Response({"message": "Account deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

        except User.DoesNotExist:
            return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
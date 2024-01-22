from .models import User
from .serializers import PortfolioUserSerializer
from djoser.views import UserViewSet


class PortfolioUserViewSet(UserViewSet):
    queryset = User.objects.all()
    serializer_class = PortfolioUserSerializer

  
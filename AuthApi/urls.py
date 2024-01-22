from django.urls import path, include
from .views import PortfolioUserViewSet

urlpatterns = [
    path('users/', PortfolioUserViewSet.as_view({'post': 'create'}), name='user-create'),
    # path('users/me/', CustomUserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update'}), name='user-detail'),
    # other Djoser URLs
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
]

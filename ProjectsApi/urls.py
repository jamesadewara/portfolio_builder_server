from django.urls import path
from .views import (
  webView,
  PortfolioListCreateView,
  PortfolioDetailView,
  PortfolioUpdateView,
  RemovePortfolioView,
  PortfolioTemplateDetailView,
  PortfolioTemplateListCreateView
)

urlpatterns = [
    path('portfolio/web/', webView, name='home'),
    path('portfolio/', PortfolioListCreateView.as_view(), name='portfolio-list-create'),
    path('portfolio/<int:pk>/', PortfolioDetailView.as_view(), name='portfolio-detail'),
    path('portfolio/update/<int:pk>/', PortfolioUpdateView.as_view(), name='portfolio-update'),
    path('portfolio/remove/<int:user>/portfolio/<int:pk>/remove/', RemovePortfolioView.as_view(), name='remove-porfolio'),
    path('templates/', PortfolioTemplateListCreateView.as_view(), name='template-list-create'),
    path('template/<int:pk>/', PortfolioTemplateDetailView.as_view(), name='template-detail'),
]
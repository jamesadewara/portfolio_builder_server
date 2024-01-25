from django.shortcuts import render
from rest_framework import generics
from .models import Portfolio, PortfolioTemplate
from .serializers import PortfolioSerializer, PortfolioTemplateSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import get_object_or_404
import json

def webView(request):
    get_template_path = "ProjectsApi/bootstrap_portfolio/index-copy.html"
    get_json_path = "/home/adewara/Documents/Freelancer-Workspace/Projects/Project Portfolio Builder/PortfolioBuilderServer/ProjectsApi/templates/ProjectsApi/bootstrap_portfolio/package.json"
    
    json_data_str = json.loads(open(get_json_path, "r").read())
    context = {'json_data': json_data_str}
    return render(request, get_template_path, context)

class PortfolioTemplateListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = PortfolioTemplate.objects.all()
    serializer_class = PortfolioTemplateSerializer

class PortfolioTemplateDetailView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = PortfolioTemplate.objects.all()
    serializer_class = PortfolioTemplateSerializer

class PortfolioListCreateView(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer


class PortfolioDetailView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

class PortfolioUpdateView(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

class RemovePortfolioView(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

    # def perform_destroy(self, instance):
    #     # Retrieve user ID and product ID from URL parameters
    #     user_id = self.kwargs.get('user_id')
    #     product_id = self.kwargs.get('pk')

    #     # Delete associated product images first
    #     instance.images.all().delete()
    #     instance.delete()

    #     # Perform any additional operations using the retrieved IDs
    #     # ...

    #     # Return a success response
    #     return Response({'message': 'Product removed successfully.'})

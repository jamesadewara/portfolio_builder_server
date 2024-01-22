from rest_framework import serializers
from .models import PortfolioTemplate, Portfolio

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'

class PortfolioTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioTemplate
        fields = '__all__'

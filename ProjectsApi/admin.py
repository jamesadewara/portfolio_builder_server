from django.contrib import admin
from .models import PortfolioTemplate, Portfolio

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'created_at']

@admin.register(PortfolioTemplate)
class PortfolioTemplateAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'created_at']


from django.contrib import admin
from .models import PortfolioCategory, PortfolioItem

admin.site.register(PortfolioItem)
admin.site.register(PortfolioCategory)

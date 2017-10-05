from django.shortcuts import get_object_or_404, render
from django.http import Http404
from .models import PortfolioItem, PortfolioCategory
from constance import config


def portfolio(request):
    items = PortfolioItem.objects.filter(published_date__isnull=False)
    categories = PortfolioCategory.objects.all()
    if config.PORTFOLIO_ENABLED:
        return render(
            request,
            'portfolio/portfolio.html',
            {'items': items, 'categories': categories}
        )
    else:
        raise Http404('Portfolio is disabled!')


def portfolio_category(request, category_slug):
    category = get_object_or_404(
        PortfolioCategory, slug=category_slug)
    category_items = PortfolioItem.objects.filter(
        category_id=category.id,
        published_date__isnull=False)
    categories = PortfolioCategory.objects.all()
    if config.PORTFOLIO_ENABLED:
        return render(
            request,
            'motionforms/portfolio_category.html',
            {'category': category, 'items': category_items,
             'categories': categories})
    else:
        raise Http404('Portfolio is disabled!')


def portfolio_item(request, category_slug, pk):
    item = get_object_or_404(PortfolioItem, pk=pk)
    category = get_object_or_404(PortfolioCategory, slug=category_slug)
    categories = PortfolioCategory.objects.all()
    if config.PORTFOLIO_ENABLED:
        return render(
            request,
            'motionforms/portfolio_item.html',
            {'portfolio_item': item, 'category': category,
             'categories': categories})
    else:
        raise Http404('Portfolio is disabled!')

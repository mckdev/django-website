from constance import config
from django.shortcuts import get_object_or_404
from django.views import generic

from .models import Homepage, Page


class HomepageView(generic.DetailView):
    model = Homepage
    template_name = 'cms/homepage.html'

    def get_object(self):
        return get_object_or_404(Homepage, pk=config.HOMEPAGE_ID)


class PageView(generic.DetailView):
    model = Page
    template_name = 'cms/page.html'

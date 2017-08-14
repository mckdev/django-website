from constance import config
from .models import Menu, SiteFooter


# Makes menu_items variable available to all templates
def menu_processor(request):
    try:
        menu = Menu.objects.get(pk=config.TOPMENU_ID)
        menu_items = menu.page_items.order_by('sorting_value')
        menu_heading = menu.heading
    except Menu.DoesNotExist:
        menu_items = None
    return {'menu_items': menu_items, 'menu_heading': menu_heading}


def footer_processor(request):
    try:
        footer = SiteFooter.objects.get(pk=config.FOOTER_ID)
    except SiteFooter.DoesNotExist:
        footer = None
    return {'footer': footer,}

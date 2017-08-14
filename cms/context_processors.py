from constance import config
from .models import Menu, SiteFooter


# Makes menu_items variable available to all templates
def menu_processor(request):
    try:
        menu_items = Menu.objects.get(pk=config.TOPMENU_ID).page_items.order_by('sorting_value')
    except Menu.DoesNotExist:
        menu_items = None
    return {'menu_items': menu_items,}


def footer_processor(request):
    try:
        footer = SiteFooter.objects.get(pk=config.FOOTER_ID)
    except SiteFooter.DoesNotExist:
        footer = None
    return {'footer': footer,}

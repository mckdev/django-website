from constance import config
from .models import GalleryCategory


# Makes menu_items variable available to all templates
def gallery_categories_processor(request):
    gallery_categories = GalleryCategory.objects.all().order_by('sorting_value')
    return {'gallery_categories': gallery_categories,}

from django.contrib import admin

from .models import Image, Video, Gallery, GalleryCategory

admin.site.register(Image)
admin.site.register(Video)
admin.site.register(Gallery)
admin.site.register(GalleryCategory)

from django.contrib import admin

from .models import Homepage, Carousel, CarouselSlide, HomepageSection, HomepageSectionContent, Page, Menu, SiteFooter

admin.site.register(Homepage)
admin.site.register(Carousel)
admin.site.register(CarouselSlide)
admin.site.register(HomepageSection)
admin.site.register(HomepageSectionContent)
admin.site.register(Page)
admin.site.register(Menu)
admin.site.register(SiteFooter)

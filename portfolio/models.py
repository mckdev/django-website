from ckeditor_uploader.fields import RichTextUploadingField
from easy_thumbnails.fields import ThumbnailerImageField
from django.db import models
from django.utils import timezone


class PortfolioItem(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    published_date = models.DateTimeField(blank=True, null=True)
    short_description = models.CharField(max_length=200)
    description = RichTextUploadingField(blank=True, null=True)
    featured_image = ThumbnailerImageField(upload_to='portfolio_featured', null=True, blank=True)
    vimeo_id = models.CharField(max_length=20, blank=True, null=True)
    category = models.ForeignKey('PortfolioCategory', on_delete=models.SET_NULL, null=True)
    noindex = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.published_date:
            self.published_date = timezone.now()
        return super(PortfolioItem, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class PortfolioCategory(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(max_length=200, blank=True, null=True)
    featured_item = models.ForeignKey('PortfolioItem', on_delete=models.SET_NULL, null=True, blank=True)
    noindex = models.BooleanField(default=False)

    def __str__(self):
        return self.title

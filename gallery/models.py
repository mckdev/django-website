from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField


class Image(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    upload = models.ImageField()

    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    youtube_id = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class GalleryCategory(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(
        max_length=200,
        unique=True,
        verbose_name='URL Slug',
        help_text='The slug will be used as URL of the page. Must be unique!'
    )
    description = models.TextField(null=True, blank=True)
    sorting_value = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Gallery(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    featured = ThumbnailerImageField(upload_to='featured', blank=True)
    images = models.ManyToManyField(Image, blank=True)
    videos = models.ManyToManyField(Video, blank=True)
    category = models.ManyToManyField(
        GalleryCategory,
        blank=True
    )

    def __str__(self):
        return self.name

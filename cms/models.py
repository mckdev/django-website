from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils import timezone


class CarouselSlide(models.Model):
    title = models.CharField(max_length=60)
    text = models.TextField()
    sorting_value = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Carousel(models.Model):
    slides = models.ManyToManyField(CarouselSlide)

    def __str__(self):
        return 'Carousel ' + str(self.pk)


class HomepageSectionContent(models.Model):
    title = models.CharField(max_length=60)
    hide_title = models.BooleanField(default=False)
    content = models.TextField()
    LEFT = 'left'
    CENTER = 'center'
    RIGHT = 'right'
    TEXT_ALIGN_CHOICES = (
        (LEFT, 'Left'),
        (CENTER, 'Center'),
        (RIGHT, 'Right'),
    )
    text_align = models.CharField(
        max_length=6,
        choices=TEXT_ALIGN_CHOICES,
        default=LEFT,
    )
    button_text = models.CharField(max_length=16, null=True, blank=True)
    button_link = models.URLField(null=True, blank=True)
    button_align = models.CharField(
        max_length=6,
        choices=TEXT_ALIGN_CHOICES,
        default=LEFT,
    )
    width = models.IntegerField(default=4)
    offset = models.IntegerField(default=0)
    sorting_value = models.IntegerField(default=0)

    class Meta:
        ordering = ['sorting_value']

    def __str__(self):
        return self.title


class HomepageSection(models.Model):
    title = models.CharField(max_length=60)
    hide_title = models.BooleanField(default=False)
    contents = models.ManyToManyField(
        HomepageSectionContent,
        blank=True
    )
    sorting_value = models.IntegerField(default=0)

    class Meta:
        ordering = ['sorting_value']

    def __str__(self):
        return self.title


class SiteFooter(models.Model):
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return 'Footer ' + str(self.pk)


class Homepage(models.Model):
    heading = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    seo_title = models.CharField(max_length=60, blank=True, null=True)
    seo_description = models.CharField(max_length=160, blank=True, null=True)
    carousel = models.ForeignKey(
        Carousel,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    sections = models.ManyToManyField(
        HomepageSection,
        blank=True
    )

    def __str__(self):
        return 'Homepage ' + str(self.pk)


class Page(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name= 'Title',
        help_text= 'Page title visible in the browser and in search engine results.'
    )

    slug = models.SlugField(
        max_length=200,
        unique=True,
        verbose_name= 'URL Slug',
        help_text='The slug will be used as URL of the page. Must be unique!'
    )

    pub_date = models.DateTimeField('date published', default=timezone.now)

    description = models.CharField(
        max_length=200,
        verbose_name= 'Short description',
        help_text='Short description of the page.'
    )
    seo_title = models.CharField(max_length=60, blank=True, null=True)
    seo_description = models.CharField(max_length=160, blank=True, null=True)

    content = RichTextUploadingField(
        verbose_name= 'Content',
        help_text='Main page content displayed in rich text.',
        blank=True,
        null=True)

    noindex = models.BooleanField(
        default=False,
        verbose_name='Don\'t index this page',
        help_text='Enable to tell search engine robots to not index this page.',
    )

    sorting_value = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Menu(models.Model):
    heading = models.CharField(max_length=20, blank=True)
    page_items = models.ManyToManyField(Page, blank=True)

    def __str__(self):
        return 'Menu ' + str(self.pk)

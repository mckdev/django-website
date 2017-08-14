from django.db import models
from django.utils import timezone


class UploadCategory(models.Model):

    class Meta:
        verbose_name_plural = "Uploads - categories"

    name = models.CharField(max_length=200, verbose_name= 'Name',
                            help_text='Provide category name.')
    short_description = models.CharField(max_length=200, blank=True)

    def has_public_uploads(self):
        for upload in self.fileupload_set.all():
            if upload.public:
                return True

    def __str__(self):
        return self.name


class Upload(models.Model):

    class Meta:
        verbose_name_plural = "Uploads"

    title = models.CharField(max_length=200, verbose_name= 'Title',
                             help_text= 'Provide name for your upload.')
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True, null=True)
    file = models.FileField()
    public = models.BooleanField(default=False)

    category = models.ManyToManyField(UploadCategory, blank=True)

    def __str__(self):
        return self.title

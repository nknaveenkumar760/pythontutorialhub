from django.db import models
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = RichTextUploadingField(blank=True, null=True)

    slug = models.SlugField(default='', blank=True)

    def save(self):
        self.slug = slugify(self.title)
        super(Post, self).save()

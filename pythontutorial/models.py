from django.db import models
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = RichTextUploadingField(blank=True, null=True)
<<<<<<< HEAD
    videoupload = RichTextUploadingField(blank=True, null=True, config_name='special',
                                         external_plugin_resources=[(
                                              'youtube',
                                              '/static/videos/ckeditor_plugins/youtube/youtube/',
                                              'plugin.js',
                                          )],
                                          )
=======
>>>>>>> 2182f3a4b8fdddf73aa0b260257e2d329ad6c815

    slug = models.SlugField(default='', blank=True)

    def save(self):
        self.slug = slugify(self.title)
        super(Post, self).save()
<<<<<<< HEAD


class VideoUploader(models.Model):

    description2 = RichTextUploadingField(blank=True, null=True, config_name='special',
                                          external_plugin_resources=[(
                                             'youtube',
                                             '/static/ckeditorplugin/video/youtube/',
                                             'plugin.js',
                                            )],
                                            )
    slug = models.SlugField(default='', blank=True)

    def save(self):
        self.slug = slugify(self.title)
        super(VideoUploader, self).save()


class Video(models.Model):
    name = models.CharField(max_length=500)
    videofile = models.FileField(upload_to='videos/', null=True, verbose_name="")
    description = RichTextUploadingField(blank=True, null=True)

    slug = models.SlugField(default='', blank=True)

    def save(self):
        self.slug = slugify(self.name)
        super(Video, self).save()
=======
>>>>>>> 2182f3a4b8fdddf73aa0b260257e2d329ad6c815


from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.template.defaultfilters import slugify


class Article(models.Model):
    title = models.CharField(max_length=500)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=2500)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.title


@receiver(models.signals.pre_save, sender=Article)
def set_slug(sender, instance, **c):
    if not instance.slug:
        instance.slug = slugify(instance.title)
from django.db import models

# Create your models here.

class Concert(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    timecreate = models.DateTimeField(auto_now_add=True)
    timeupdate = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')

    def __str__(self):
        return self.name
from django.utils import timezone
from django.utils.text import slugify
from django.db import models
from django.contrib.auth.models import User




class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name= 'عنوان')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles', verbose_name='نویسنده')
    body = models.TextField(verbose_name='توضیحات')
    slug = models.SlugField(blank=True, unique=True, allow_unicode=True, verbose_name='اسلاگ')
    status = models.BooleanField(default=True, verbose_name='وضعیت')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    publish = models.DateTimeField(default=timezone.now, verbose_name='تاریخ انتشار')

    class Meta:
        ordering = ('-created', )
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'


    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title,allow_unicode=True)
        super(Article, self).save()

    def __str__(self):
        return self.title

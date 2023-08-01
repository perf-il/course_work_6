from transliterate import slugify

from django.db import models
from users.models import User, NULLABLE


class Blog(models.Model):
    title_name = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.CharField(default=slugify(str(title_name)), max_length=150)
    content = models.TextField(verbose_name='Текст', **NULLABLE)
    preview = models.ImageField(upload_to='blog/preview', default='preview/default.JPG', verbose_name='Изображение')
    data_creating = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='автор')

    def delete(self, *args, **kwargs):
        self.is_published = False
        self.save()

    def __str__(self):
        return f'{self.title_name}'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блог'
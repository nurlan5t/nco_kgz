from django.db import models

class News(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name='Дата обновления')
    image = models.ImageField(null=True)
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = "Новости"
    def __str__(self):
        return self.title


from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование категории')
    descriptions = models.TextField(verbose_name='Описание категории', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование товара')
    descriptions = models.TextField(verbose_name='Описание товара', blank=True, null=True)
    image = models.ImageField(upload_to='catalog/image')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория')
    price = models.FloatField(blank=False, null=False, default=0, verbose_name='Цена')
    date_create = models.DateField(auto_now_add=True)
    date_change = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['category', 'name']

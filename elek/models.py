from django.db import models

class Elektro(models.Model):
    model = models.CharField('Модель', max_length=50)
    mark = models.CharField('Марка', max_length=50)
    price = models.IntegerField('Цена')
    color = models.CharField('Цвет', max_length=50)
    description = models.TextField('+')
    img = models.ImageField(upload_to='photo')

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Електро'
        verbose_name_plural = 'Електроники'


class Nout(models.Model):
    model = models.CharField('Модель', max_length=50)
    mark = models.CharField('Марка', max_length=50)
    price = models.IntegerField('Цена')
    color = models.CharField('Цвет', max_length=50)
    description = models.TextField('+')
    img = models.ImageField(upload_to='photo')

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Ноутбук'
        verbose_name_plural = 'Ноутбуктар'


class Acsessuar(models.Model):
    model = models.CharField('Модель', max_length=50)
    mark = models.CharField('Марка', max_length=50)
    price = models.IntegerField('Цена')
    color = models.CharField('Цвет', max_length=50)
    description = models.TextField('+')
    img = models.ImageField(upload_to='photo')

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Аксессуар'
        verbose_name_plural = 'Аксессуары'





from django.db import models

class PersonCategory(models.Model):
    name = models.CharField(verbose_name="Кем является", max_length=255)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория людей'
        verbose_name_plural = 'Категории людей'


class Person(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=255)
    last_name = models.CharField(verbose_name='Фамилия', max_length=255)
    email = models.EmailField(verbose_name='Email адрес', unique=True, max_length=255)
    telephone = models.CharField(verbose_name='Номер телефона', max_length=255)
    birthday = models.DateField(verbose_name='Дата рождения')
    category = models.ForeignKey(
        PersonCategory,
        related_name="person",
        verbose_name='Категория',
        on_delete=models.SET_NULL,##Удаляем категорию, а чел остается
        null=True
    )

    
    def __str__(self):
        return f'{self.first_name}, {self.last_name}'
    
    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'


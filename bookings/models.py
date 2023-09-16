from django.db import models


class Field(models.Model):
    number = models.IntegerField(verbose_name="Номер поля")
    bio = models.TextField(verbose_name="Описание")
    field_image = models.ImageField(verbose_name="Фото поля", upload_to="field_images/", default=False)
    
    class Meta:
        verbose_name = "Поле"
        verbose_name_plural = "Поля"

    def __str__(self):
        return str(self.number)


class Booking(models.Model):
    date = models.DateField(verbose_name='Дата брони')
    time = models.TimeField(verbose_name='Время брони')
    field = models.ForeignKey(Field, on_delete=models.CASCADE,verbose_name="Поле для брони")
    
    class Meta:
        verbose_name = "Бронь"
        verbose_name_plural = "Брони"

    def __str__(self):
        return 'Booking for {} and {}'.format(self.date, self.time)
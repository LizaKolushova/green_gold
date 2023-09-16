from django.db import models
from people.models import Person


class Event(models.Model):
    name = models.TextField(verbose_name="Номер поля", max_length = 255)
    event_image = models.ImageField(verbose_name="Фото события", upload_to="event_images/", default=False)
    date = models.DateField(verbose_name='Дата события')
    time = models.TimeField(verbose_name='Время события')
    text = models.TextField(verbose_name="Описание события")

    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"

    def __str__(self):
        return str(self.name)


class BookingEvent(models.Model):
    participant = models.ForeignKey(Person, on_delete=models.CASCADE,verbose_name="Участник")
    event = models.ForeignKey(Event,on_delete=models.CASCADE,verbose_name="Бронь события")
    
    class Meta:
        verbose_name = "Бронирование события"
        verbose_name_plural = "Бронирование события"
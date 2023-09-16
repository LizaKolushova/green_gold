from rest_framework import viewsets
from .models import *
from .serializers import *
from django.http import HttpResponse
from .tasks import send_email


def home(request):
    send_email.delay()
    return HttpResponse('<h1> отправка сообщения на почту </h1>')


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['create']:
            return EventCreateSerializer
        return EventSerializer
    
class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingEventSerializer
    queryset = BookingEvent.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['create']:
            return BookingEventCreateSerializer
        return BookingEventSerializer
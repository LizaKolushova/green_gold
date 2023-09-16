from rest_framework import viewsets
from .models import *
from .serializers import *
from django.http import HttpResponse
from .tasks import send_email


def home(request):
    send_email.delay()
    return HttpResponse('<h1> отправка сообщения на почту </h1>')


class FieldViewSet(viewsets.ModelViewSet):
    serializer_class = FieldSerializer
    queryset = Field.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['create']:
            return FieldCreateSerializer
        return FieldSerializer
    
class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['create']:
            return BookingCreateSerializer
        return BookingSerializer
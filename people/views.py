from rest_framework import viewsets
from .models import *
from .serializers import *
from django.http import HttpResponse
from .tasks import send_email


def home(request):
    send_email.delay()
    return HttpResponse('<h1> отправка сообщения на почту </h1>')


class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['create']:
            return PersonCreateSerializer
        return PersonSerializer
    
class PersonCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = PersonCategorySerializer
    queryset = PersonCategory.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['create']:
            return PersonCategoryCreateSerializer
        return PersonCategorySerializer
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'name', 'date', 'time', 'text')


class BookingEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingEvent
        fields = ( 'id', 'participant', 'event')
        

class EventCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('name', 'date', 'time', 'text')


class BookingEventCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingEvent
        fields = ('participant', 'event')
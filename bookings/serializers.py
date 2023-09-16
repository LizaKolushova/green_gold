from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = ('id', 'number', 'bio')


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ( 'id', 'date', 'time', 'field')
        

class FieldCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = ('number', 'bio')


class BookingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('date', 'time', 'field')
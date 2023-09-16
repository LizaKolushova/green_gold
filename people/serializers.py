from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")


class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField()


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ("id", "first_name", "last_name", "email", "telephone", "category")


class PersonCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonCategory
        fields = ("id", "name")


class PersonCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = (
            "first_name",
            "last_name",
            "email",
            "telephone",
            "category",
            "birthday",
        )

    def validate_number(self, value):
        if len(value) > 11:
            raise serializers.ValidationError(
                f"Номер телефона состоит из 11 символов, вы ввели {len(value)}"
            )
        return value


class PersonCategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonCategory
        fields = ("name",)

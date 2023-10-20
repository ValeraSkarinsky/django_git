from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Car

class Serializercar(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['name']

    # def validate_country(self, value):
    #     # Пример валидации поля "country"
    #     valid_countries = ["Korea", "Germany", "Japan"]
    #     if value not in valid_countries:
    #         raise serializers.ValidationError("Недопустимая страна производства.")
    #     return value
    #
    # def validate_countеry(self, value):
    #     # Пример валидации поля "country"
    #     valid_name = ["BMW X5", "Hyundai Sonata", "Toyota Camry"]
    #     if value not in valid_name:
    #         raise serializers.ValidationError("Недопустимая марка производства.")
    #     return value
class SeriaLizeruser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
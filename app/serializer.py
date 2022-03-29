from rest_framework import serializers
from .models import Menu,Mahsulot

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model=Menu
        fields='__all__'


class MahsulotSerializer(serializers.ModelSerializer):
    class Meta:
        model=Mahsulot
        fields='__all__'
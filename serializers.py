from rest_framework import serializers
from .models import *

class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = "__all__"


class StaticPropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = StaticProperty
        fields = "__all__"


class DynamicPropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = DynamicProperty
        fields = "__all__"
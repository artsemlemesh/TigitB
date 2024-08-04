from rest_framework import serializers
from .models import MainTab, SubTab


class SubTabSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTab
        fields = ['id', 'label', 'content']

class MainTabSerializer(serializers.ModelSerializer):
    sub_tabs = SubTabSerializer(many=True, read_only=True)
    
    class Meta:
        model = MainTab
        fields = ['id', 'label', 'sub_tabs']
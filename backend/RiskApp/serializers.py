from rest_framework import serializers
from .models import Risk, PolicySuggestion

class RiskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Risk
        fields = '__all__'

class PolicySuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PolicySuggestion
        fields = '__all__'

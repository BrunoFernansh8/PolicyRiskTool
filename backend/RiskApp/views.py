from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets
from .models import Risk, PolicySuggestion
from .serializers import RiskSerializer, PolicySuggestionSerializer

class RiskViewSet(viewsets.ModelViewSet):
    queryset = Risk.objects.all()
    serializer_class = RiskSerializer

class PolicySuggestionViewSet(viewsets.ModelViewSet):
    queryset = PolicySuggestion.objects.all()
    serializer_class = PolicySuggestionSerializer
    
def create(self, request, *args, **kwargs):
    response = super().create(request, *args, **kwargs)
    risk = self.get_object()
    score = risk.calculate_risk_score()

    if score >= 6:
        PolicySuggestion.objects.create(
            risk=risk,
            suggestion="Consider immediate action for high-priority risk."
        )
    elif 3 <= score < 6:
        PolicySuggestion.objects.create(
            risk=risk,
            suggestion="Review and mitigate moderate-priority risk."
        )
    return response


from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Risk(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    risk_type = models.CharField(max_length=50)
    impact = models.CharField(max_length=50)
    severity = models.CharField(max_length=10, choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')])
    likelihood = models.CharField(max_length=10, choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')])
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def calculate_risk_score(self):
        severity_score = {'High': 3, 'Medium': 2, 'Low': 1}
        likelihood_score = {'High': 3, 'Medium': 2, 'Low': 1}
        return severity_score[self.severity] * likelihood_score[self.likelihood]

class PolicySuggestion(models.Model):
    risk = models.ForeignKey(Risk, on_delete=models.CASCADE)
    suggestion = models.TextField()


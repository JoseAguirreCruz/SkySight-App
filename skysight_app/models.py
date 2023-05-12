from django.db import models
from django.contrib.auth.models import User

class Tracker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)

class WeatherData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    condition = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    maxtemp_c = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    mintemp_c = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    maxwind_kph = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    totalprecip_mm = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    uv = models.DecimalField(max_digits=5, decimal_places=2, null=True)


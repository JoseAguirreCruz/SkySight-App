from django.db import models
from django.contrib.auth.models import User


class Tracker(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def form_valid(self, form):
    form.instance.user = self.request.user  
    return super().form_valid(form)

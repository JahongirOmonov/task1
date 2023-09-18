from django.db import models
from django.contrib.auth.models import User




class TV(models.Model):
    name = models.CharField(max_length=200, default='sony')
    SN = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self) -> str:
        return self.name


class simCard(models.Model):
    comName = models.CharField(max_length=201, default='uzm')
    number = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self) -> str:
        return self.comName
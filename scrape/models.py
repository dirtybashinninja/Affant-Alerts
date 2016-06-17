from django.db import models
from django.utils import timezone


class Device(models.Model):
    device = models.CharField(max_length=200, default='None')
    clientName = models.CharField(max_length=200, default='None')
    avgResolutionTime = models.BigIntegerField(default=0)  #This is the avg time the device is down per alert
    avgFailureTime = models.BigIntegerField(default=0)  #This is the average time between failures
    uptime =  models.BigIntegerField(default=0) #This will be the percentage that the device is up

    def __str___(self):
        return self.device

    def calcResolutiontime(self):
        return 1

    def calcFailuretime(self):
        return 1

    def calcUptime(self):
        return 1


class Alert(models.Model):
    deviceName = models.CharField(max_length=200, default='None')
    clientName = models.CharField(max_length=200, default='None')
    alertID = models.IntegerField(default=0)
    timeOpened = models.DateTimeField(default=timezone.now)
    timeClosed = models.DateTimeField(default=timezone.now)
    device = models.ForeignKey(Device, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.clientName, self.deviceName, self.alertID

    

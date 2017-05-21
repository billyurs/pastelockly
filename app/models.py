from django.db import models

class MessageDetails(models.Model):
    key = models.CharField(max_length=1000)
    message_data = models.CharField(max_length=1000)
    protected =models.CharField(max_length=1000)
    encrypted_data = models.CharField(max_length=1000)
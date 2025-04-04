from django.db import models

class Log(models.Model):
    key_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

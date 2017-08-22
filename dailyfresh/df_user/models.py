from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=40)

    def __str__(self):
        return self.username.encode('utf-8')
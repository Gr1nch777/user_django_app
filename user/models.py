from django.db import models


class User(models.Model):

    username = models.CharField(max_length=50)
    e_mail = models.CharField(max_length=50)

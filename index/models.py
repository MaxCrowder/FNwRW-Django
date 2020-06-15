from django.db import models


class Podcast(models.Model):
    uid = models.CharField(max_length=50)
    date = models.CharField(max_length=10)
    titleText = models.CharField(max_length=50)
    streamUrl = models.CharField(max_length=2083)
    redirectionUrl = models.CharField(max_length=2083)


class Donation(models.Model):
    name = models.CharField(max_length=50)
    date = models.CharField(max_length=10)
    amount = models.FloatField()
    email = models.CharField(max_length=50)


class Email(models.Model):
    email = models.CharField(max_length=50)

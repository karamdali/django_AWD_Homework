from django.db import models

# Create your models here.

class StockData(models.Model):
    ticker_symbol = models.CharField(max_length=10)
    date = models.DateField()
    open_price = models.FloatField()
    close_price = models.FloatField()

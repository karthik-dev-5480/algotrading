# stocks/models.py
from django.db import models

class Stock(models.Model):
    symbol = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.symbol

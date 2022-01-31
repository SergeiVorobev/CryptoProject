from django.db import models


# Create your models here.
class Strategy(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name of Strategy', blank=True)
    long_strategy = models.BooleanField(blank=True)
    total_amount_of_coin = models.FloatField(verbose_name='Total amount of coin', blank=True)
    number_of_orders = models.IntegerField(verbose_name='Number of orders needed to make', blank=True)
    start_price = models.FloatField(verbose_name='Current price of the coin', blank=True)
    first_margin = models.FloatField(verbose_name='Margin of the first order', blank=True)
    max_set_margin = models.FloatField(verbose_name='Total percentage of order set', blank=True)
    use_bnb = models.BooleanField(blank=True)

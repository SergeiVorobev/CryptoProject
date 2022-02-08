from django.db import models
from django.utils import timezone
import datetime
from datetime import date
from django.core.exceptions import ValidationError

# Create your models here.
BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))


class Strategy(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name of Strategy', blank=True)
    long_strategy = models.BooleanField(choices=BOOL_CHOICES)
    pair = models.CharField(max_length=20, verbose_name='Pair', blank=True)
    date_strategy = models.DateField(verbose_name='Strategy Date', default=timezone.now)
    total_amount_of_coin = models.FloatField(verbose_name='Total amount of coin', blank=True)
    number_of_orders = models.IntegerField(verbose_name='Number of orders needed to make', blank=True)
    margin = models.FloatField(verbose_name='Orders margin', blank=True, default=0)
    start_price = models.FloatField(verbose_name='Start price of the coin', blank=True)
    first_margin = models.FloatField(verbose_name='Margin of the first order', blank=True)
    max_set_margin = models.FloatField(verbose_name='Total percentage of order set', blank=True)
    use_bnb = models.BooleanField(choices=BOOL_CHOICES)
    profit = models.FloatField(verbose_name='Profit percentage',  blank=True, default=0)
    # current_price = models.FloatField(verbose_name='Current price of the coin', blank=True)


    def save(self, *args, **kwargs):
        if self.date_strategy < datetime.date.today():
            raise ValidationError("The date cannot be in the past!")
        super(Strategy, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    @property
    def is_past_due(self):
        return date.today() > self.date_strategy


# Generated by Django 4.0.1 on 2022-02-08 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0002_strategy_margin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='strategy',
            name='margin',
        ),
    ]
# Generated by Django 4.0.1 on 2022-02-08 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='strategy',
            name='margin',
            field=models.FloatField(blank=True, default=None, null=True, verbose_name='Orders margin'),
        ),
    ]

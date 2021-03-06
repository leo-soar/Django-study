# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-03-28 03:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0003_book_pub'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='desc',
        ),
        migrations.AddField(
            model_name='book',
            name='market_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='零售价'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(default='', max_length=50, unique=True, verbose_name='书名'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteapp', '0002_auto_20140929_0438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='subcategory',
            field=models.ForeignKey(default=None, blank=True, to='siteapp.Category', null=True),
        ),
    ]

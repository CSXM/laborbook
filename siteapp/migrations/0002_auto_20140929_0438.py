# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='subcategory',
            field=models.ForeignKey(to='siteapp.Category', null=True),
        ),
    ]

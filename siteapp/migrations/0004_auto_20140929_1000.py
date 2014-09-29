# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteapp', '0003_auto_20140929_0721'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='subcategory',
            new_name='parent_category',
        ),
    ]

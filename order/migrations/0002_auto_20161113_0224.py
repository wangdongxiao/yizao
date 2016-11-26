# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='name',
            field=models.CharField(default='', max_length=20, verbose_name='\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='projectclass',
            name='desc',
            field=models.TextField(default='', verbose_name='\u63cf\u8ff0'),
        ),
    ]

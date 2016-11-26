# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20161113_0224'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4', null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4', null=True),
        ),
        migrations.AddField(
            model_name='projectclass',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4', null=True),
        ),
        migrations.AddField(
            model_name='projectclass',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4', null=True),
        ),
    ]

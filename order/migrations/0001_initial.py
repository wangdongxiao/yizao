# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('desc', models.TextField(verbose_name='\u63cf\u8ff0')),
                ('price', models.IntegerField(default=0, verbose_name='\u4ef7\u683c')),
            ],
            options={
                'verbose_name': '\u68c0\u6d4b\u9879\u76ee',
                'verbose_name_plural': '\u68c0\u6d4b\u9879\u76ee',
            },
        ),
        migrations.CreateModel(
            name='ProjectClass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='\u540d\u79f0')),
                ('desc', models.TextField(verbose_name='\u63cf\u8ff0')),
            ],
            options={
                'verbose_name': '\u68c0\u6d4b\u9879\u76ee\u5206\u7c7b',
                'verbose_name_plural': '\u68c0\u6d4b\u9879\u76ee\u5206\u7c7b',
            },
        ),
        migrations.AddField(
            model_name='project',
            name='project',
            field=models.ForeignKey(verbose_name='\u6240\u5c5e\u9879\u76ee\u5206\u7c7b', to='order.ProjectClass'),
        ),
    ]

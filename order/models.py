# coding=utf8
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User


class BaseMode(models.Model):
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name=u'创建时间')
    update_time = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=u'修改时间')

    class Meta:
        abstract = True
        ordering = ['-update_time', '-create_time']


class ProjectClass(BaseMode):
    name = models.CharField(verbose_name='名称', max_length=20)
    desc = models.TextField(verbose_name='描述', default='')

    class Meta:
        verbose_name = '检测项目分类'
        verbose_name_plural = '检测项目分类'


class Project(BaseMode):
    project_class = models.ForeignKey(ProjectClass, verbose_name='所属项目分类')
    name = models.CharField(verbose_name='名称', max_length=20, default='')
    desc = models.TextField(verbose_name='描述')
    price = models.IntegerField(verbose_name='价格', default=0)

    class Meta:
        verbose_name = '检测项目'
        verbose_name_plural = '检测项目'


class OrderInformation(BaseMode):
    user = models.ForeignKey(User, verbose_name='用户')
    username = models.CharField(max_length=20, verbose_name='称呼')
    project = models.ManyToManyField(Project, verbose_name='预约项目')
    order_time = models.DateTimeField(null=True, blank=True, verbose_name='预约时间')
    telephone = models.CharField(max_length=20, verbose_name='用户手机')

# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import absolute_import

from django.contrib import admin

from .models import Project, ProjectClass


@admin.register(ProjectClass)
class ProjectClassAdmin(admin.ModelAdmin):
    list_display = ['name', 'desc']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'desc', 'price', 'project_class']

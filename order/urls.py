# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import absolute_import

from django.conf.urls import patterns, url

from . import views as _views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'project_class', _views.ProjectClassViewSet)
router.register(r'project', _views.ProjectViewSet)

urlpatterns = router.urls

# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import absolute_import

from rest_framework import generics
from rest_framework import viewsets

from .models import ProjectClass, Project, OrderInformation
from .serializers import ProjectClassSerializer, ProjectSerializer, OrderInformationSerializer


class ProjectClassViewSet(viewsets.ModelViewSet):
    model = ProjectClass
    serializer_class = ProjectClassSerializer
    queryset = model.objects.all()


class ProjectViewSet(viewsets.ModelViewSet):
    model = Project
    serializer_class = ProjectSerializer
    queryset = model.objects.all()


class OrderInformationViewSet(viewsets.ModelViewSet):
    model = OrderInformation
    serializer_class = OrderInformationSerializer
    queryset = model.objects.all()


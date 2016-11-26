# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from rest_framework import serializers

from .models import ProjectClass, Project, OrderInformation


class ProjectClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectClass
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class OrderInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderInformation
        fields = '__all__'

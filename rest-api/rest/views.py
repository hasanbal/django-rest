# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from models import Driver
from rest_framework import viewsets
from rest.serializers import DriverSerializer
# Create your views here.

class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def test(request):
    return HttpResponse(rr(5))

def rr(n):
    return n



# coding: utf-8
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import loader, Context
from django.conf import settings
from django.template import RequestContext

# Create your views here.

def home(request):
    return render(request, 'index.html')
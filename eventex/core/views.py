# coding: utf-8
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import loader, Context
from django.conf import settings
from django.template import RequestContext
from eventex.core.models import Speaker
from django.shortcuts import get_object_or_404

# Create your views here.

def home(request): return render(request, 'index.html')

def speaker_detail(request, slug): 
	speaker = get_object_or_404(Speaker, slug=slug)
	context = {'speaker':speaker}
	return render(request, 'core/speaker_detail.html', context)
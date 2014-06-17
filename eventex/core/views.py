# coding: utf-8
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import loader, Context
from django.conf import settings
from django.template import RequestContext
from eventex.core.models import Speaker, Talk
from django.shortcuts import get_object_or_404
#from datetime import time

# Create your views here.

def home(request): 
	return render(request, 'index.html', {'get_query_set':Talk.objects.get_query_set})

def speaker_detail(request, slug): 
	speaker = get_object_or_404(Speaker, slug=slug)
	context = {'speaker':speaker,}
	return render(request, 'core/speaker_detail.html', context)

def talk_list(request): 
	#midday = time(12) -> refatorando
	context = {
			'morning_talks':Talk.objects.at_morning(),
			'afternoon_talks':Talk.objects.at_afternoon(),
	}
	return render(request, 'core/talk_list.html', context)

def talk_detail(request, pk):
	talk = get_object_or_404(Talk, pk=pk)
	context = {'talk':talk,}
	return render(request, 'core/talk_detail.html', context)
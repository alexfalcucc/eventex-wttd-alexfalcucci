# conding: utf-8
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription

# Create your views here.


"""
def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            obj = form.save()
            #obj = Subscription(**form.cleaned_data) -refatorado com form.save()
            #form.full_clean() -> o form.is_valid tem atribuido
            #obj.save()
            return HttpResponseRedirect('/inscricao/%d/' % obj.pk)
        else:
            return render(request, 'subscriptions/subscription_form.html', 
                                    {'form':form})
    else:
            return render(request, 'subscriptions/subscription_form.html', 
                                    {'form':SubscriptionForm()})"""
# Refatorando a View subscribe.

def subscribe(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)

def new(request):
    return render(request, 'subscriptions/subscription_form.html', 
                            {'form': SubscriptionForm()})
def create(request):
    form = SubscriptionForm(request.POST)
    if not form.is_valid():
        return render(request, 'subscriptions/subscription_form.html', 
                                {'form': form})
    obj = form.save()
    return HttpResponseRedirect('/inscricao/%d/' %obj.pk)

def detail(request, pk):
    subscription = get_object_or_404(Subscription, pk=pk)
    return render(request, 'subscriptions/subscription_detail.html', {'subscription':subscription})
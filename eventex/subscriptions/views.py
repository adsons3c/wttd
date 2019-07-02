from django.shortcuts import render
from eventex.subscriptions.forms import SubscriptionsForm


def subscribe(request):
    context = {'form': SubscriptionsForm()}
    return render(request, 'subscriptions/subscription_form.html', context)

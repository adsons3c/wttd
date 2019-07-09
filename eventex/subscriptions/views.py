from django.http import HttpResponseRedirect
from django.shortcuts import render
from eventex.subscriptions.forms import SubscriptionsForm
from django.core import mail
from django.template.loader import render_to_string


def subscribe(request):
    if request.method == "POST":
        body = render_to_string('subscriptions/subscription_email.txt', context)
        mail.send_mail('Confirmação de inscrição',
                       'Message',
                       'contato@eventex.com.br',
                       ['contato@eventex.com.br', 'adsonemanuels3c@gmail.com'])
        return HttpResponseRedirect('/inscricao/')

    else:
        context = {'form': SubscriptionsForm()}
        return render(request, 'subscriptions/subscription_form.html', context)

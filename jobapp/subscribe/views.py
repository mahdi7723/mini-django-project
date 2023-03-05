from django.shortcuts import render, redirect

from subscribe.forms import SubscribeForm
from subscribe.models import Subscribe


# Create your views here.
def subscribe(request):
    subscribe_form = SubscribeForm()
    email_error_empty = ""
    if request.POST:
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()
            return redirect('thank_you')
    context = {"form": subscribe_form, "email_error_empty": email_error_empty}
    return render(request, 'subscribe/subscribe.html', context)


def thank_you(request):
    context = {}
    return render(request, "subscribe/thank_you.html", context)

from django import forms
from django.utils.translation import gettext_lazy as _
from subscribe.models import Subscribe


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = '__all__'
        labels = {
            'first_name': _('Enter first name'),
            'last_name': _('Enter last name'),
            'email': _('Enter email')
        }
        error_messages = {
            'first_name': {
                'required': _ ('you can not move forward without first name')
            }
        }

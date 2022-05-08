#from django.forms import ModelForm
#from .models import Contact


#class ContactForm(ModelForm):
#    class Meta:
#        model = Contact
#        fields = '__all__'

from django import forms
from .models import Contact, NewletterSubscriber


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewletterSubscriber
        fields = ['email', ]
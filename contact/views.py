from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import NewletterSubscriber
from .forms import ContactForm, NewsletterForm


# Create views for contact.


def contact(request):
    """ A view to handle the user contact form """

    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for contacting us. We will \
                be in touch shortly.')
            return redirect(reverse('contact'))

    context = {
        'form': form
    }

    return render(request, 'contact/contact.html', context)

# a function to newsletter subscriptions.


def newsletter(request):
    """ A view to handle the user newsletter subscription """
    form = NewsletterForm()

    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            if NewletterSubscriber.objects.filter(
                    email=instance.email).exists():
                messages.error(request, 'You are already Subscribed')
            else:
                instance.save()
                messages.success(request, 'Thank you for subscribing to our \
                    newsletter!')
                return redirect(reverse('home'))

    context = {
        'form': form,
    }

    return render(request, 'contact/newsletter.html', context)

# a function to newsletter unsubscriptions.


def newsletter_unsub(request):
    """ A view to handle newsletter unsubscriptions """
    form = NewsletterForm()

    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            if NewletterSubscriber.objects.filter(
                    email=instance.email).exists():
                NewletterSubscriber.objects.filter(
                    email=instance.email).delete()
                messages.success(request, 'You have successfully unsubscribed \
                    from our newsletter.We are happy to welcome you \
                        back again.')
                return redirect(reverse('home'))
            else:
                messages.error(request, 'Sorry the emain address you entered is not correct. \
                    Please check it and entered correctly.')

    context = {
        'form': form,
    }

    return render(request, 'contact/newsletter-unsubscribe.html', context)

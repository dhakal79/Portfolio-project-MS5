
from django.db import models

#class Contact(models.Model):
#    email = models.EmailField()
#   subject = models.CharField(max_length=255)
#   message = models.TextField()

#    def __str__(self):
#        return self.email

class Contact(models.Model):
    """ A Model for the contact form """

    full_name = models.CharField(max_length=254, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    subject = models.CharField(max_length=50, null=False, blank=False)
    message = models.TextField(max_length=254, null=False, blank=False)


class NewletterSubscriber(models.Model):
    """ A Model for the newsletter subscription form """

    email = models.EmailField(max_length=254, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
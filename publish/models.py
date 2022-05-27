from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

"""classbased model for posting the news"""


class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date="publish")
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="news_post")
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-publish", ]

    def __str__(self):
        return self.title + ' |' + str(self.author)

    def get_absolute_url(self):
        return reverse("news_post",
                       args=[self.publish.year, self.publish.month,
                             self.publish.day, self.publish.hour,
                             self.publish.minute, self.slug])

    def get_edit_url(self):
        return reverse("edit_post",
                       args=[self.publish.year, self.publish.month,
                             self.publish.day, self.publish.hour,
                             self.publish.minute, self.slug])

    def get_delete_url(self):
        return reverse("delete_post",
                       args=[self.publish.year, self.publish.month,
                             self.publish.day, self.publish.hour,
                             self.publish.minute, self.slug])

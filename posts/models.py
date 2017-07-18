from django.db import models

# from django.conf import settings
# from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse


class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return "/posts/%s/" %(self.id)
        return reverse("posts:detail", kwargs={"id": self.id})

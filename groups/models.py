from django.db import models

from posts.models import Post

from django.core.urlresolvers import reverse


class Group(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(unique=True)
    contact_updated = models.DateField(auto_now=False, auto_now_add=True)
    group_status = models.CharField(max_length=20)
    admin = models.CharField(max_length=20)
    admin_status = models.CharField(max_length=20)
    frequency = models.IntegerField()  # allowed post frequency
    frq_scale = models.CharField(max_length=20, blank=True)
    obs = models.TextField(blank=True)

    posts = models.ManyToManyField(Post, through='control.Control')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("groups:detail", kwargs={"id": self.id})

    class Meta:
        ordering = ['-id']

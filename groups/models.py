from django.db import models
from django.conf import settings

from posts.models import Post

from django.core.urlresolvers import reverse

STATUS_CHOICES = getattr(settings, "STATUS_CHOICES", ())
STATUS_LIST = getattr(settings, "STATUS_LIST", ())


class GroupManager(models.Manager):
    def filter_by_status(self, status):
        return super(GroupManager, self).filter(status__contains=status)


class Group(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(unique=True)
    contact_updated = models.DateField(auto_now=False, auto_now_add=True)
    admin = models.CharField(max_length=20)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    frequency = models.IntegerField()  # allowed post frequency
    frq_scale = models.CharField(max_length=20, blank=True)
    obs = models.TextField(blank=True)

    posts = models.ManyToManyField(Post, through='control.Control')

    objects = GroupManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("groups:detail", kwargs={"id": self.id})

    class Meta:
        ordering = ['-id']

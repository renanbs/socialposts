from django.db import models

from posts.models import Post

from django.core.urlresolvers import reverse


class Group(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(unique=True)
    contact_updated = models.DateField(auto_now=False, auto_now_add=True)
    admin = models.CharField(max_length=20)

    s = ('------', 'ok', 'nok', 'waiting in', 'waiting admin', 'admin ignored')
    Status = (
        (1, 'ok'),
        (2, 'nok'),
        (3, 'waiting in'),
        (4, 'waiting admin'),
        (5, 'admin ignored'),
    )

    status = models.CharField(max_length=20, choices=Status)
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

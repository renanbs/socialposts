from django.db import models

from groups.models import Group
from posts.models import Post

from django.core.urlresolvers import reverse


class ControlManager(models.Manager):
    def filter_by_group_status(self, status):
        qs = super(ControlManager, self).filter(group__status__contains=status)
        return qs

    def filter_by_date_range(self, initial, final):
        qs = super(ControlManager, self).filter(published__range=[initial, final])
        return qs


class Control(models.Model):
    published = models.DateField(auto_now=False, auto_now_add=False)

    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE)
    group = models.ForeignKey('groups.Group', on_delete=models.CASCADE)

    objects = ControlManager()

    def __str__(self):
        return str(self.published)

    def get_absolute_url(self):
        return reverse("control:control_list")

    class Meta:
        # unique_together = ("post", "group")
        ordering = ['published']

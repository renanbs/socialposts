from django.db import models

from groups.models import Group
from posts.models import Post

from django.core.urlresolvers import reverse


# class ControlManager(models.Manager):
#     def all(self):
#         qs = super(ControlManager, self).filter(parent=None)
#         return qs
#
#     def filter_by_instance(self, instance):
#         content_type = ContentType.objects.get_for_model(instance.__class__)
#         obj_id = instance.id
#         qs = super(ControlManager, self).filter(content_type=content_type, object_id=obj_id).filter(parent=None)
#         return qs


class Control(models.Model):
    published = models.DateField(auto_now=False, auto_now_add=False)

    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE)
    group = models.ForeignKey('groups.Group', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.published)

    # def get_absolute_url(self):
    #     return reverse("groups:detail", kwargs={"id": self.id})
    #
    class Meta:
        ordering = ['group']

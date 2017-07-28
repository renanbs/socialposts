from django.db import models

from django.core.urlresolvers import reverse


class Control(models.Model):
    published = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return str(self.published)

    # def get_absolute_url(self):
    #     return reverse("groups:detail", kwargs={"id": self.id})
    #
    # class Meta:
    #     ordering = ['-id']

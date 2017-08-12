from django.conf.urls import url

from .views import (
    control_list,
    control_create,
)

urlpatterns = [
    url(r'^$', control_list, name="list"),
    url(r'^create/$', control_create),
    # url(r'^(?P<id>\d+)/$', group_detail, name="detail"),
    # url(r'^(?P<id>\d+)/edit/$', group_update, name="update"),
    # url(r'^(?P<id>\d+)/delete/$', group_delete),
]

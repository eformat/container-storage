from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'api/register/(?P<node_id>[a-zA-Z0-9\-]+)/?$', views.register_node, name='register_node'),
    url(r'api/snapshot/(?P<node_id>[a-zA-Z0-9\-]+)/?$', views.post_snapshot, name='snapshot'),
]

from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^remove/(?P<id>\d+)$', views.remove),
    url(r'^add_course$', views.create),
]
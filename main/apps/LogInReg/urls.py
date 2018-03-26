from django.contrib import admin
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.validate),
    url(r'^adder$', views.add),
    url(r'^exit$', views.goingaway)
]
# url(r'^$', views.toindex, name='my_index'),
#     url(r'^this_app/new$', views.new, name='my_new'),
#     url(r'^this_app/(?P<id>\d+)/edit$', views.edit, name='my_edit'),
#     url(r'^this_app/(?P<id>\d+)/delete$', views.delete, name='my_delete'),
#     url(r'^this_app/(?P<id>\d+)$', views.show, name='my_show'),
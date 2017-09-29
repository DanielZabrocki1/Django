from django.conf.urls import url

import people
from . import views

app_name = 'people'

urlpatterns = (

    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    url(r'^add/$', views.PersonCreate.as_view(), name='person_add'),

    url(r'^(?P<pk>[0-9]+)/update/$', views.PersonUpdate.as_view(), name='update'),

    url(r'^(?P<pk>[0-9]+)/delete/$', views.PersonDelete.as_view(), name='person_delete'),

    url(r'^info/$', views.info, name='info'),

)
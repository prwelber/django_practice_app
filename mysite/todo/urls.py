from django.conf.urls import url


from . import views

app_name = 'todo'
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^(?P<item_id>[0-9]+)/$', views.show, name='show'),
    url(r'^(?P<item_id>[0-9]+)/edit/$', views.edit, name='edit'),
    url(r'^new/$', views.new, name='new'),
    url(r'^(?P<item_id>[0-9]+)/update/$', views.update, name='update'),
    url(r'^create/$', views.create, name='create'),
    url(r'^delete/$', views.delete, name='delete')
]

# in these URL's, anything after '^' represents anything after todo/

from django.conf.urls import patterns, url
from landing import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^landing/contact/$', views.contact, name='contact'),

]

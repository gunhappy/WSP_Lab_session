from django.conf.urls import url
#from django.contrib import admin
from .import views

urlpatterns = [
url(r'^$', views.index, name='Index'),
url(r'^showdata/$', views.showdata),
url(r'^select/$', views.select),
url(r'^update/$', views.update),
url(r'^doUpdate/$', views.doUpdate),
url(r'^delete/$', views.delete),
url(r'^login/$', views.login),
url(r'^doLogin/$', views.doLogin),
url(r'^logout/$', views.logout),
]

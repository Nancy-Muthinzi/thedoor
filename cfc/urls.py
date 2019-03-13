from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.welcome, name='welcome'),
    url(r'^about/', views.about, name='about'),
    url(r'^program/', views.program, name='program'),
    url(r'^sermon/', views.sermon, name='sermon'),
    url(r'^blog/', views.blog, name='blog'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^search/', views.search_results, name='search_results'),
]
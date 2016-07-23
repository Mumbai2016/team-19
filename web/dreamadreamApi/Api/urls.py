from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', 'Api.views.index', name='index'),
]

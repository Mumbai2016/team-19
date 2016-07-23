from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'Api.views.index', name='index'),

    url(r'^webapp/register/', 'Api.controllers.webapp.auth.register', name='register'),
    url(r'^webapp/login/', 'Api.controllers.webapp.auth.login', name='login'),
]

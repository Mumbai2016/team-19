from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'Api.views.index', name='index'),

    url(r'^webapp/register/', 'Api.controllers.webapp.auth.register', name='register'),
    url(r'^webapp/login/', 'Api.controllers.webapp.auth.login', name='login'),

    url(r'^webapp/member/list', 'Api.controllers.webapp.member.list', name='list_members'),
    url(r'^webapp/member/get/(?P<id>[0-9]+$)', 'Api.controllers.admin.members.member_detail', name='member_detail'),
    url(r'^webapp/member/delete/(?P<id>[0-9]+$)', 'Api.controllers.admin.members.member_delete', name='member_delete'),

    url(r'exotel/make_exotel_call/$',
        'Api.controllers.admin.exotelcalls.make_exotel_call_task', name='make_exotel_calls'),
]

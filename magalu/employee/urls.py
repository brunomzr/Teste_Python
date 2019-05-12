from django.conf.urls import url

from . import views

urlpatterns = [
        url(
            r'^employee/(?P<pk>[0-9]+)/$',
            views.get_delete_update_employee,
            name='get_delete_update_employee'
        ),
        url(
            r'^employee/$',
            views.get_post_employee,
            name='get_post_employee'
        ),
        url(
            r'^department/$',
            views.get_post_department,
            name='get_post_department'
        )
    ]

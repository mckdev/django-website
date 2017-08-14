from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    # Password Reset
    url(r'^password_reset/$',
        auth_views.password_reset,
        name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done,
        name='password_reset_done'),
    url(r'^password_reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^password_reset/complete/$', auth_views.password_reset_complete,
        name='password_reset_complete'),

    # Password Change
    url(r'^password_change/$', views.password_change, name='password_change'),
    url(r'^password_changed/$', views.password_changed, name='password_changed'),

    # Login and logout
    url(r'^login/$', auth_views.login, name='login',
        kwargs={'redirect_authenticated_user': True}),
    url(r'^logout/$', auth_views.logout, name='logout',
        kwargs={'next_page': 'login'}),

    # Signup process
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),

    # User profile
    url(r'^profile/$', views.profile_view, name='profile_view'),
    url(r'^profile/edit/$', views.profile_edit, name='profile_edit'),
    url(r'^profile/image/', include('avatar.urls')),
]

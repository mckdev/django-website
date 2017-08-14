from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'
urlpatterns = [
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^edit_profile/$', views.update_profile, name='update_profile'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', auth_views.login, name='login',
        kwargs={'redirect_authenticated_user': True}),
    url(r'^logout/$', auth_views.logout, name='logout',
        kwargs={'next_page': 'accounts:login'}),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^change_password/$', views.change_password, name='change_password'),
    url(r'^password_changed/$', views.password_changed, name='password_changed'),
    url(r'^change_password/$', views.change_password, name='change_password'),
    url(r'^profile_image/', include('avatar.urls')),
]
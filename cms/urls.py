from django.conf.urls import url

from . import views

app_name = 'cms'
urlpatterns = [
    url(r'^$', views.HomepageView.as_view(), name='homepage' ),
    url(r'^(?P<slug>[\w-]+)/$', views.PageView.as_view(), name='page'),
]

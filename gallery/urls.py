from django.conf.urls import url

from . import views

app_name = 'gallery'
urlpatterns = [
    url(r'^$', views.GalleryIndex.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.GalleryDetail.as_view(), name='detail'),
    url(r'^category/(?P<slug>[\w-]+)/$', views.GalleryCategoryView.as_view(), name='category'),
]

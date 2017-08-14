from django.views import generic

from .models import Gallery, GalleryCategory


class GalleryIndex(generic.ListView):
    model = Gallery
    template_name = 'gallery/index.html'
    context_object_name = 'galleries'


class GalleryDetail(generic.DetailView):
    model = Gallery
    template_name = 'gallery/detail.html'


class GalleryCategoryView(generic.ListView):
    model = Gallery
    template_name = 'gallery/category.html'
    context_object_name = 'galleries'

    def get_queryset(self):
        return Gallery.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(GalleryCategoryView, self).get_context_data(**kwargs)
        context['category'] = GalleryCategory.objects.get(slug=self.kwargs['slug'])
        return context

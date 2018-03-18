from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView
from zdjeciogram.forms import AddPhotoForm
from zdjeciogram.models import Photo


class MainView(ListView):
    model = Photo
    ordering = ['-creation_date']


class PhotoView(DetailView):
    model = Photo


class AddPhotoView(LoginRequiredMixin, FormView):
    form_class = AddPhotoForm
    success_url = reverse_lazy('main')
    template_name = 'zdjeciogram/photo_form.html'
    def form_valid(self, form):
        description = form.cleaned_data['description']
        path = form.cleaned_data['path']
        Photo.objects.create(
            description=description,
            author=self.request.user,
            path=path
        )
        return super(AddPhotoView, self).form_valid(form)


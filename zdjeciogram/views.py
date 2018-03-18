from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import ModelForm
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView

from zdjeciogram.models import Photo


class MainView(ListView):
    model = Photo
    ordering = ['-creation_date']


class PhotoView(DetailView):
    model = Photo


class AddPhotoView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['path', 'description']

    def form_valid(self, form: ModelForm):
        path = form.cleaned_data['path']
        description = form.cleaned_data['description']
        user = self.request.user
        p = Photo.objects.create(path=path, description=description, author_id = user.id)

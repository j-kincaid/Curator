from pdb import post_mortem
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import ModelForm
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Artwork
from .forms import EntriesForm

class EntriesListView(ListView):
    model = Artwork
    context_object_name = "entries"
    template_name = "entries/entries_list.html"


class EntriesDetailView(LoginRequiredMixin, DetailView):
    model = Artwork
    context_object_name = "entry"
    template_name = "entries/entries_detail.html"
    login_url = '/login'

"""
Using ModelForm for database-driven features. The docs say 'You do not even need to provide a success_url for CreateView or UpdateView - they will use get_absolute_url() on the model object if available'.

"""
class EntriesForm(LoginRequiredMixin, ModelForm):
    class Meta:
        model = Artwork
        fields = ['artwork_title', 
        # 'medium', 
        'height_in_inches', 'width_in_inches', 'depth_in_inches', 'year_completed']
        login_url = '/login'


class EntriesCreateView(LoginRequiredMixin, CreateView):
    model = Artwork
    template_name = 'entries/artwork_update_form.html'
    fields = ['artwork_title', 
    # 'medium', 
    'height_in_inches', 'width_in_inches', 'depth_in_inches', 'year_completed']
    login_url = '/login'


class EntriesUpdateView(LoginRequiredMixin, UpdateView):
    model = Artwork
    fields = ['artwork_title', 
    # 'medium', 
    'height_in_inches', 'width_in_inches', 'depth_in_inches', 'year_completed']
    template_name_suffix = '_update_form'


class EntriesDeleteView(LoginRequiredMixin, DeleteView):
    model = Artwork
    success_url = '/artballot/entries'
    template_name_suffix = '_confirm_delete'
    login_url = '/login'



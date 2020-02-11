from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import MovieManagerPage,ContactUs


# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class MovieListView(ListView):
    model = MovieManagerPage
    template_name = 'movie_list.html'

class MovieDetailView(DetailView):
    model = MovieManagerPage
    template_name = 'movie_detail.html'

class ContactUsPageView(CreateView):
    model = ContactUs
    template_name = 'contact.html'
    fields = ['name','email','phone','query', 'message',]
    success_url = reverse_lazy('thankyou')

class ThankYouPageView(TemplateView):
    model = ContactUs
    template_name = 'thankyoupage.html'

class ManagerCreateView(CreateView):
    model = MovieManagerPage
    template_name = 'manager_create.html'
    fields = ['title','storyline','web_url','ratings','photo',]
    success_url = reverse_lazy('movie')

class ManagerUpdateView(UpdateView):
    model = MovieManagerPage
    fields = ('storyline', 'ratings','photo')
    template_name = 'manager_edit.html'


class ManagerDeleteView(DeleteView):
    model = MovieManagerPage
    template_name  = 'manager_delete.html'
    success_url = reverse_lazy('movie')


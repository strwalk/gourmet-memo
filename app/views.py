from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Gourmet

# Create your views here.
class ReviewList(ListView):
    model = Gourmet
    fields = '__all__'
    template_name = 'app/index.html'

class ReviewCreate(CreateView):
    model = Gourmet
    fields = ['restaurant_name', 'memo', 'rating']
    template_name = 'app/create.html'
    success_url = reverse_lazy('list')

class ReviewUpdate(UpdateView):
    model = Gourmet
    fields = ['restaurant_name', 'memo', 'rating']
    template_name = 'app/update.html'
    success_url = reverse_lazy('list')

class ReviewDelete(DeleteView):
    model = Gourmet
    template_name = 'app/delete.html'
    success_url = reverse_lazy('list')
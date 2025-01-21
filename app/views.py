from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Gourmet

class ReviewList(LoginRequiredMixin, ListView):
    model = Gourmet
    fields = '__all__'
    template_name = 'app/index.html'
    login_url = reverse_lazy('login')

class ReviewCreate(LoginRequiredMixin, CreateView):
    model = Gourmet
    fields = ['restaurant_name', 'memo', 'rating']
    template_name = 'app/create.html'
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('list')

class ReviewUpdate(LoginRequiredMixin, UpdateView):
    model = Gourmet
    fields = ['restaurant_name', 'memo', 'rating']
    template_name = 'app/update.html'
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('list')

class ReviewDelete(LoginRequiredMixin, DeleteView):
    model = Gourmet
    template_name = 'app/delete.html'
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('list')

class UserLogin(LoginView):
    template_name = 'app/login.html'

    def get_success_url(self):
        return reverse_lazy('list')

class UserLogout(LogoutView):
    def get_success_url(self):
        return reverse_lazy('login')


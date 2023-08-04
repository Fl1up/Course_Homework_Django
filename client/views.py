from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from client.forms import ClientForms
from client.models import Client


class ClientListView(ListView):
    model = Client
    template_name = 'client/client_list.html'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class ClientDetailView(DetailView):
    model = Client
    template_name = 'client/client_detail.html'


class ClientCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Client
    form_class = ClientForms
    permission_required = "client.add_client"
    success_url = reverse_lazy('client:list')


class ClientUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForms
    permission_required = "client.change_client"
    success_url = reverse_lazy('client:list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user:
            raise Http404
        return self.object


class ClientDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('client:list')
    permission_required = "client.delete_client"


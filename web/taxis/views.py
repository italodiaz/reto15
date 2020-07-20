from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from .models import Distrito, Vehiculo, Viaje, Favoritos
from .forms import VehiculoForm, FavoritosForm
from django.urls import reverse_lazy


# Create your views here.
class Home(TemplateView):
    template_name = 'taxis/index.html'


class ListVehiculo(ListView):
    model = Vehiculo
    template_name = 'taxis/vehiculo/list_vehiculo.html'
    queryset = Vehiculo.objects.all()
    context_object_name = 'vehiculos'


class CreateVehiculo(CreateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'taxis/vehiculo/create_vehiculo.html'
    success_url = reverse_lazy('taxis:list.vehiculo')


class UpdateVehiculo(UpdateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'taxis/vehiculo/update_vehiculo.html'
    success_url = reverse_lazy('taxis:list.vehiculo')


class DeleteVehiculo(DeleteView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'taxis/vehiculo/delete_vehiculo.html'
    success_url = reverse_lazy('taxis:list.vehiculo')
    
    def get_context_data(self, **kwargs):
        vehiculo = Vehiculo.objects.get(id=self.kwargs.get('pk'))
        context = super(DeleteVehiculo, self).get_context_data(**kwargs)
        context['vehiculo'] = vehiculo
        return context


class ListFavoritos(ListView):
    model = Favoritos
    template_name = 'taxis/favoritos/list_favoritos.html'
    queryset = Favoritos.objects.all()
    context_object_name = 'favoritos'


class CreateFavoritos(CreateView):
    model = Favoritos
    form_class = FavoritosForm
    template_name = 'taxis/favoritos/create_favoritos.html'
    success_url = reverse_lazy('taxis:list.favoritos')


class UpdateFavoritos(UpdateView):
    model = Favoritos
    form_class = FavoritosForm
    template_name = 'taxis/favoritos/update_favoritos.html'
    success_url = reverse_lazy('taxis:list.favoritos')


class DeleteFavoritos(DeleteView):
    model = Favoritos
    form_class = FavoritosForm
    template_name = 'taxis/favoritos/delete_favoritos.html'
    success_url = reverse_lazy('taxis:list.favoritos')
    
    def get_context_data(self, **kwargs):
        favoritos = Favoritos.objects.get(id=self.kwargs.get('pk'))
        context = super(DeleteFavoritos, self).get_context_data(**kwargs)
        context['favoritos'] = favoritos
        return context

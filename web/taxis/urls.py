from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (
    Home, ListVehiculo, CreateVehiculo, UpdateVehiculo, DeleteVehiculo,
    ListFavoritos, CreateFavoritos, UpdateFavoritos, DeleteFavoritos
)


urlpatterns = [
    path('', login_required(Home.as_view()), name='index'),
    path('vehiculo/list', login_required(ListVehiculo.as_view()), name='list.vehiculo'),
    path('vehiculo/create', login_required(CreateVehiculo.as_view()), name='create.vehiculo'),
    path('vehiculo/update/<int:pk>', login_required(UpdateVehiculo.as_view()), name='update.vehiculo'),
    path('vehiculo/delete/<int:pk>', login_required(DeleteVehiculo.as_view()), name='delete.vehiculo'),
    path('favoritos/list', login_required(ListFavoritos.as_view()), name='list.favoritos'),
    path('favoritos/create', login_required(CreateFavoritos.as_view()), name='create.favoritos'),
    path('favoritos/update/<int:pk>', login_required(UpdateFavoritos.as_view()), name='update.favoritos'),
    path('favoritos/delete/<int:pk>', login_required(DeleteFavoritos.as_view()), name='delete.favoritos'),
]

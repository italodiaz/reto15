from django.contrib import admin
from .models import Vehiculo, Favoritos, Distrito, Viaje

# Register your models here.

class VehiculoAdmin(admin.ModelAdmin):
    list_display = ['placa','conductor','marca','modelo','tipo','color' ]
    search_fields = ['placa','conductor']

class DistritoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']
    search_fields = ['nombre']


class FavoritosAdmin(admin.ModelAdmin):
    list_display = ['id', 'usuario','direccion', 'distrito']
    search_fields = ['usuario','distrito']


class Viajedmin(admin.ModelAdmin):
    list_display = ['fecha_hora_solicitado', 'estado','usuario','vehiculo',
                'distrito_recojo','direccion_recojo','distrito_destino','direccion_destino',
                'puntos_valoracion']
    search_fields = ['estado','usuario','vehiculo']

admin.site.register(Vehiculo,VehiculoAdmin)
admin.site.register(Distrito,DistritoAdmin)
admin.site.register(Favoritos,FavoritosAdmin)
admin.site.register(Viaje,Viajedmin)

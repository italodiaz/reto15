from django.forms import ModelForm, TextInput, Select, NumberInput
from .models import Vehiculo, Favoritos

def get_labels(fields):
    labels  = {}
    for field in list(fields):
        labels[field] = field.capitalize().replace('_', ' ')
    return labels

def get_widgets(fields):
    widgets = {}
    for key, value in fields.items():
        attrs={
            'class': 'form-control',
            'id': key
        }
        if value == 'Select':
            widgets[key] = Select(attrs=attrs)
        elif value == 'NumberInput':
            widgets[key] = NumberInput(attrs=attrs)
        elif value == 'TextInput':
            field = key.replace('_', ' ')
            attrs['placeholder'] = f'Ingrese {field}'
            widgets[key] = TextInput(attrs=attrs)
        else:
            pass
    return widgets


class VehiculoForm(ModelForm):
    class Meta:
        fields_var = {
            'placa': 'TextInput',
            'conductor': 'Select',
            'marca': 'TextInput',
            'modelo': 'TextInput',
            'color': 'TextInput'
        }
        model = Vehiculo
        fields = fields_var.keys()
        labels = get_labels(fields_var.keys())
        widgets = get_widgets(fields_var)

class FavoritosForm(ModelForm):
    class Meta:
        fields_var = {
            'usuario':'Select',
            'distrito':'Select',
            'direccion':'TextInput'
        }
        model = Favoritos
        fields = fields_var.keys()
        labels = get_labels(fields_var.keys())
        widgets = get_widgets(fields_var)

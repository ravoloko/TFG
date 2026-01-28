from django import forms
from .models import LineaPresupuesto

class LineaPresupuestoForm(forms.ModelForm):
    class Meta:
        model = LineaPresupuesto
        # Elegimos los campos que el usuario rellenará
        fields = ['concepto', 'monto', 'tipo', 'categoria']
        # Añadimos estilos para que se vea bien
        widgets = {
            'concepto': forms.TextInput(attrs={'class': 'border p-2 w-full'}),
            'monto': forms.NumberInput(attrs={'class': 'border p-2 w-full'}),
            'tipo': forms.Select(attrs={'class': 'border p-2 w-full'}),
            'categoria': forms.Select(attrs={'class': 'border p-2 w-full'}),
        }
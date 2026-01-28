from django.db import models
from django.contrib.auth.models import User

# Nueva tabla para clasificar los gastos/ingresos
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    # Un campo simple para que el frontend sepa qué icono poner (ej: 'fa-home')
    icono = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.nombre

class Presupuesto(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    total_calculado = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return self.nombre

class LineaPresupuesto(models.Model):
    TIPO_CHOICES = [
        ('INGRESO', 'Ingreso (+)'),
        ('GASTO', 'Gasto (-)'),
    ]

    presupuesto = models.ForeignKey(Presupuesto, on_delete=models.CASCADE, related_name='lineas')
    # Relación con Categoria: Si se borra la categoría, la línea se queda pero sin categoría (null)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    concepto = models.CharField(max_length=200)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, default='GASTO')
    # Añadimos fecha para poder hacer filtros temporales
    fecha = models.DateField(auto_now_add=True) # Se pone la fecha de hoy automáticamente

    def __str__(self):
        return f"{self.tipo}: {self.concepto} ({self.monto}€)"
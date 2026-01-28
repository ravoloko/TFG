from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import LineaPresupuesto

@receiver([post_save, post_delete], sender=LineaPresupuesto)
def recalcular_total(sender, instance, **kwargs):
    # 1. Buscamos el presupuesto padre
    presupuesto = instance.presupuesto
    
    # 2. Empezamos el balance en 0
    balance = 0
    
    # 3. Recorremos todas las líneas y sumamos o restamos según el tipo
    for linea in presupuesto.lineas.all():
        if linea.tipo == 'INGRESO':
            balance += linea.monto
        else:
            balance -= linea.monto
            
    # 4. Actualizamos el total del presupuesto y guardamos
    presupuesto.total_calculado = balance
    presupuesto.save()
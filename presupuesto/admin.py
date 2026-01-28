from django.contrib import admin

# Register your models here.
# Importamos tus modelos desde el archivo models.py de la misma carpeta
from .models import Presupuesto, LineaPresupuesto, Categoria
# Esto le dice a Django: "Muestra estas tablas en el panel de administrador"
admin.site.register(Presupuesto)
admin.site.register(LineaPresupuesto)
admin.site.register(Categoria)

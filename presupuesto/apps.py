from django.apps import AppConfig


class PresupuestoConfig(AppConfig):
    name = 'presupuesto'

from django.apps import AppConfig

class PresupuestoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'presupuesto'

    # Esta función se ejecuta cuando Django se inicia
    def ready(self):
        # Importamos el archivo de señales que acabas de crear
        import presupuesto.signals

from django.urls import path
from . import views

urlpatterns = [
    # Ruta para ver un presupuesto específico y añadirle gastos/ingresos
    path('presupuesto/<int:pk>/', views.detalle_presupuesto, name='detalle_presupuesto'),
]
urlpatterns = [
    # ... tus otras urls ...
    path('linea/eliminar/<int:pk>/', views.eliminar_linea, name='eliminar_linea'),
]
urlpatterns = [
    # ... otras urls ...
    path('linea/editar/<int:pk>/', views.editar_linea, name='editar_linea'),
]
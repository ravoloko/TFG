from django.shortcuts import render, redirect, get_object_or_404
from .models import Presupuesto
from .forms import LineaPresupuestoForm
from .models import LineaPresupuesto

def detalle_presupuesto(request, pk):
    # 1. Buscamos el presupuesto por su ID (su "DNI")
    presupuesto = get_object_or_404(Presupuesto, pk=pk)
    
    # 2. Si el usuario envía el formulario (pulsa el botón de añadir)
    if request.method == 'POST':
        form = LineaPresupuestoForm(request.POST)
        if form.is_valid():
            nueva_linea = form.save(commit=False)
            nueva_linea.presupuesto = presupuesto # La vinculamos a este presupuesto
            nueva_linea.save() # Al guardar aquí, saltará tu SIGNAL de cálculo
            return redirect('detalle_presupuesto', pk=pk)
    else:
        form = LineaPresupuestoForm()

    # 3. Enviamos todo al HTML
    return render(request, 'presupuesto/detalle.html', {
        'presupuesto': presupuesto,
        'form': form,
        'lineas': presupuesto.lineas.all()
    })

def eliminar_linea(request, pk):
    # 1. Buscamos la línea que se quiere borrar
    linea = get_object_or_404(LineaPresupuesto, pk=pk)
    # 2. Guardamos el ID del presupuesto para poder volver a la misma página
    presupuesto_id = linea.presupuesto.id
    # 3. La borramos (esto activará el Signal post_delete para recalcular el total)
    linea.delete()
    # 4. Volvemos a la vista del presupuesto
    return redirect('detalle_presupuesto', pk=presupuesto_id)

def editar_linea(request, pk):
    # 1. Obtenemos la línea que queremos editar usando su ID
    linea = get_object_or_404(LineaPresupuesto, pk=pk)
    presupuesto_id = linea.presupuesto.id
    
    # 2. Cargamos el formulario con los datos que ya existen (instance=linea)
    if request.method == 'POST':
        form = LineaPresupuestoForm(request.POST, instance=linea)
        if form.is_valid():
            form.save() # Al guardar, el Signal actualizará el total automáticamente
            return redirect('detalle_presupuesto', pk=presupuesto_id)
    else:
        form = LineaPresupuestoForm(instance=linea)
    
    # 3. Usamos un template sencillo para editar
    return render(request, 'presupuesto/editar_linea.html', {
        'form': form,
        'linea': linea
    })

# Create your views here.

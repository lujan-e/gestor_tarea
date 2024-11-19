from django.shortcuts import render, redirect
from .froms import TareaForm
from .models import Tarea

def vista(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vistas')
    else:
        form = TareaForm()
    tareas = Tarea.objects.all()
    return render(request, 'tarea/vista.html', {'form': form, 'tareas': tareas})

def marcar_completada(request, tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    tarea.completada = True
    tarea.save()
    return redirect('vistas')



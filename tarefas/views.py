from django.shortcuts import render, get_object_or_404, redirect
from . models import Tarefa
from .forms import TarefaForm

# Create your views here.


def inicio(request):
    tarefas_list = Tarefa.objects.all().order_by('-created_at')
    return render(request, 'tarefas/index.html', {'var_tarefas': tarefas_list})


def TarefaView(request, id):
    tarefa = get_object_or_404(Tarefa, pk=id)
    return render(request, 'tarefas/view_tarefa.html', {'tarefa': tarefa})


def novaTarefa(resquest):
    if resquest.method == 'POST':
        form = TarefaForm(resquest.POST)
        form.save()
        return redirect('/')

    else:
        form = TarefaForm()
        return render(resquest, 'tarefa/addTarefa.html', {'form': form})

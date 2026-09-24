# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Destino, MensagemContato

def catalogo_destinos(request):
    destinos = Destino.objects.all()
    return render(request, 'turismo/catalogo.html', {'destinos': destinos})

def detalhes_destino(request, destino_id):
    destino = get_object_or_404(Destino, id=destino_id)
    return render(request, 'turismo/detalhes.html', {'destino': destino})

def solicitar_orcamento(request, destino_id):
    destino = get_object_or_404(Destino, id=destino_id)
    
    if request.method == 'POST':
        MensagemContato.objects.create(
            nome=request.POST.get('nome'),
            email=request.POST.get('email'),
            destino_interesse=destino.nome,
            mensagem=request.POST.get('mensagem')
        )
        return redirect('catalogo_destinos')

    return render(request, 'turismo/orcamento.html', {'destino': destino})
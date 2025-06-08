from django.shortcuts import render
from .models import PortfolioItem, PostBlog
from .forms import ContatoForm, OrcamentoForm

def home(request):
    return render(request, 'sitecore/home.html')

def quem_somos(request):
    return render(request, 'sitecore/quem_somos.html')

def servicos(request):
    return render(request, 'sitecore/servicos.html')

def portfolio(request):
    projetos = PortfolioItem.objects.all()
    return render(request, 'sitecore/portfolio.html', {'projetos': projetos})

def contato(request):
    form = ContatoForm(request.POST or None)
    if form.is_valid():
        # Aqui você pode enviar email ou salvar o contato
        form = ContatoForm()  # limpa o formulário
    return render(request, 'sitecore/contato.html', {'form': form})

def orcamento(request):
    form = OrcamentoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        # Lógica para salvar ou enviar dados do orçamento
        form = OrcamentoForm()
    return render(request, 'sitecore/orcamento.html', {'form': form})

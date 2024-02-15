from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Produtos
from .forms import ProdutoForm

def home(request):
    produtos = Produtos.objects.all()
    return render(request, 'home.html', {'produtos': produtos})

def add_produto(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProdutoForm()
    return render(request, 'add_produto.html', {'form': form})

def edit_produto(request, id):
    produto = Produtos.objects.get(id=id)
    if request.method == "POST":
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'edit_produto.html', {'form': form})

def delete_produto(request, id):
    produto = Produtos.objects.get(id=id)
    if request.method == "POST":
        produto.delete()
        return redirect('home')
    return render(request, 'delete_produto.html', {'produto': produto})
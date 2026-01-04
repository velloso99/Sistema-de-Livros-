from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return HttpResponse('login')

def cadastro(request):
    return render(request, 'cadastro.html')

def valida_cadastro(request):
    
    return HttpResponse()
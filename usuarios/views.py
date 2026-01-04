from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from django.shortcuts import redirect
from hashlib import sha256

def login(request):
    return HttpResponse('login')

def cadastro(request):
    return render(request,'cadastro.html')

def valida_cadastro(request):
    nome= request.POST.get('nome')
    email= request.POST.get('email')  
    senha= request.POST.get('senha')
    usuario = Usuario.objects.filter(email=email)

    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        return redirect('/auth/cadastro/?status=1')
    
    if len(senha) < 8:
        return redirect('/auth/cadastro/?status=2')

    if len(usuario) > 0:
        return redirect('/auth/cadastro/?status=3')
    try:
        senha = sha256(senha.encode()).hexdigest()
        usuario= Usuario(nome=nome, email=email, senha=senha)
        usuario.save()
        return redirect('/auth/cadastro/?statud=0')
    except:
        return redirect('/auth/cadastro/?statud=4')

    return HttpResponse(f"{nome}{senha}{email}")
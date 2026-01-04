from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name ='Login'),
    path('cadastro/', views.cadastro, name='Cadastro'),
    path('validar_cadastro/', views.valida_cadastro, name ='valida_cadastro')

]
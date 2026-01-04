from usuarios.models import Usuario
from django.contrib import admin


admin.site.register(Usuario)

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    readonly_fields = {'nome', 'email', 'senha'}
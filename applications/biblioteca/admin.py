from django.contrib import admin
from .models import Autor, Libros 

class AutorAdmin(admin.ModelAdmin): 
    list_display = (
        'nombre',
        'nacionalidad',
        'id'
    )

    search_fields = ('nombre', 'nacionalidad')

# Hacemos lo mismo que para Autor:
class LibrosAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'resume',
        'autor',
        'id'
    )

    search_fields = ('title',) # La coma es imprescindible ya que es una tupla.
    # Si queremos poner un nuevo filtro para autores usamos un nuevo atributo:
    list_filter = ('autor',) # Esto filtrará en base a lo que queramos añadir, como por ejemplo el autor.

admin.site.register(Autor, AutorAdmin)
# Vinculamos el nuevo decorador:
admin.site.register(Libros, LibrosAdmin)

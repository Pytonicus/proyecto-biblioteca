from django.shortcuts import render
from django.views.generic import(
    TemplateView,
    ListView,
    CreateView # Importamos una nueva vista generica para introducir datos
)

from .models import Autor, Libros

class ListaAutores(ListView):
    template_name = 'biblioteca/lista-autores.html'
    model = Autor
    context_object_name = 'autores'

class ListaLibrosAutores(ListView):
    template_name = 'biblioteca/lista-libros.html'
    model = Libros 
    context_object_name = 'libros'
    def get_queryset(self):
        id = self.kwargs['pk']
        lista = Libros.objects.filter( 
            autor = id
        )
        return lista

# vamos a crear la clase con la vista:
class AddAutor(CreateView):
    # Asigmanos el template:
    template_name = 'biblioteca/add-autor.html'
    # Ahora añadimos el modelo en el cual vamos a registrar al autor:
    model = Autor
    # Ahora vamos a solicitar los campos para hacer el registro:
    fields = ['nombre', 'nacionalidad']
    # Se recomienda establecer que va a pasar una vez se complete el registro:
    success_url = '/' # nos enviará a la ruta raiz.
    

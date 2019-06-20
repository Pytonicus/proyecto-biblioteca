from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView # Importamos la librería genérica Listview
)

class IndexView(TemplateView):
    template_name = "home/index.html"
    print('=============== URL de Prueba ================') 

# Esta vista es un poco más compleja que TemplateView:
class ListaLibros(ListView): #Creamos una clase que heredará de ListView
    template_name = "home/lista.html"
    # Creamos una lista manual asignandole a queryset un array:
    queryset = ['El quijote', 'El código da vinci', 'Oscuros', 'Sherlock Holmes']
    # Ahora vamos a establecer con que nombre vamos a manipular la lista de arriba:
    context_object_name = "libros"
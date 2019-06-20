from django.db import models

class Autor(models.Model): 
    nombre = models.CharField('Nombres', max_length=80)
    nacionalidad = models.CharField(blank=True, max_length=100) 

    
    def __str__(self):
        return self.nombre 

# Creamos una nueva tabla:
class Libros(models.Model):
    title = models.CharField('Título', blank=False, max_length=150)
    resume = models.TextField('Resumen', blank=True) # Textfield admite un número indeterminado de caracteres
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE) # Creamos una clave foranea para vincular la tabla Autor con la tabla libros, le pasamos el parámetro on_delete obligatorio de modo que cuando se elimine un autor sus libros también se borrarán en cascada.

    def __str__(self):
        return self.title
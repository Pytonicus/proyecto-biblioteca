from django.urls import path, re_path

app_name = "home_app"

from . import views

urlpatterns = [
    path('index', views.IndexView.as_view(), name="index"),
    # Introducimos la nueva url a la vista ListaLibros:
    path('libros', views.ListaLibros.as_view(), name="lista")
]
from django.urls import path, include
from .views import ListarTareas

urlpatterns = [
    path('', ListarTareas.as_view())
]
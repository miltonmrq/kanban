from django.urls import path, include
from .views import ListarTareaView, ListarTableroView

urlpatterns = [
    path('', ListarTareaView.as_view()),
    path('Tarea/<int:pk>/', views.post_detail, name='post_detail'),

]
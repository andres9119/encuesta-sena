from django.urls import path
from .views import encuesta_view, gracias_view, nueva_encuesta

urlpatterns = [
    path('encuesta/', encuesta_view, name='encuesta'),
    path('gracias/', gracias_view, name='gracias'),
    path('nueva_encuesta/', nueva_encuesta, name='nueva_encuesta'),
]

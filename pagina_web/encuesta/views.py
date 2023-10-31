from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import RespuestaEncuesta
from .pdf_generator import generate_pdf
import os
from datetime import datetime
from django.conf import settings


def encuesta_view(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        cargo = request.POST.get('cargo')
        pregunta1 = request.POST.get('pregunta1')
        pregunta2 = request.POST.get('pregunta2')
        pregunta3 = request.POST.get('pregunta3')
        pregunta4 = request.POST.get('pregunta4')
        pregunta5 = request.POST.get('pregunta5')
        pregunta6 = request.POST.get('pregunta6')
        pregunta7 = request.POST.get('pregunta7')
        pregunta8 = request.POST.get('pregunta8')
        pregunta9 = request.POST.get('pregunta9')
        pregunta10 = request.POST.get('pregunta10')
        pregunta11 = request.POST.get('pregunta11')
        pregunta12 = request.POST.get('pregunta12')

        # Guardar en el modelo RespuestaEncuesta
        respuesta = RespuestaEncuesta(
            nombre=nombre,
            cargo=cargo,
            pregunta1=pregunta1,
            pregunta2=pregunta2,
            pregunta3=pregunta3,
            pregunta4=pregunta4,
            pregunta5=pregunta5,
            pregunta6=pregunta6,
            pregunta7=pregunta7,
            pregunta8=pregunta8,
            pregunta9=pregunta9,
            pregunta10=pregunta10,
            pregunta11=pregunta11,
            pregunta12=pregunta12,
            # Asigna los valores de los demás campos aquí
        )
        respuesta.save()

        # Guardar los datos en un diccionario
        data = {
            'Nombre': nombre,
            'Cargo': cargo,
            '1- ¿Cómo nació la idea de los desayunos sorpresa?': pregunta1,
            '2- ¿De qué productos se conforman los desayunos?': pregunta2,
            '3- ¿Cómo hacen los clientes para solicitar un servicio?': pregunta3,
            '4- ¿Cómo es el medio de pago?': pregunta4,
            '5- ¿Que medios de comunicacion usas para promocionar los productos?': pregunta5,
            '6- describe el proceso de empaque y envio': pregunta6,
            '7-¿Cuanto tiempo llevan en este negocio?': pregunta7,
            '8- se han presentado devoluciones del producto, y como es el procesos que realizas?': pregunta8,
            '9- ¿Cuantos tipos de desayunos manejan y que otros productos tienen disponibles a los clientes ?': pregunta9,
            '10- ¿Para que tipo de eventos se realizan los desayunos sopresas u otros?': pregunta10,
            '11- ¿Cuantas personas hacen parte del negocio?': pregunta11,
            '12- ¿existe otro proceso el cual quisieras mencionar?': pregunta12,
            # Otras preguntas y sus respuestas
        }

        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')  # Genera una marca de tiempo
        # Generar el PDF y guardar en la ruta deseada

        filename = f'respuestas_formulario_{timestamp}.pdf'
        output_filename = os.path.join(
            settings.MEDIA_ROOT, 'pdf_encuestas', filename)
        generate_pdf(data, output_filename)

        # Redireccionar a la página de agradecimiento
        return HttpResponseRedirect('/gracias/')
    return render(request, 'encuesta.html')


def gracias_view(request):
    return render(request, 'gracias.html')


def nueva_encuesta(request):
    # Redirigir al formulario de la encuesta
    return redirect('encuesta')

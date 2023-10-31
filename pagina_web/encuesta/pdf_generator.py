from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def generate_pdf(data, output_filename):
    # Crear un lienzo (canvas) para el PDF con un tamaño de página
    c = canvas.Canvas(output_filename, pagesize=letter)

    # Configurar la apariencia y el contenido del PDF
    c.drawString(100, 700, "Encuesta")  # Título del documento
    y_position = 680  # Posición vertical inicial para los datos de la encuesta

    # Iterar sobre los datos de la encuesta para agregarlos al PDF
    for key, value in data.items():
        c.drawString(100, y_position, f"{key}: {value}")
        y_position -= 20  # Espaciado entre líneas

    # Guardar el PDF
    c.save()

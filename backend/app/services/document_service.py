from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
from datetime import datetime

from app.utils.document_context import construir_contexto_documento

env = Environment(
    loader=FileSystemLoader("app/templates")
)

def generar_constancia(alumno):

    template = env.get_template(
        "certificados/constancia_estudios.html"
    )

    contexto = construir_contexto_documento(alumno)

    html = template.render(
        **contexto,
        fecha=datetime.now().strftime("%d/%m/%Y")
    )

    output = f"tmp/constancia_{alumno.id}.pdf"

    HTML(string=html).write_pdf(output)

    return output
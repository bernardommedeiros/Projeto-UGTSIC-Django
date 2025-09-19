from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile

def generate_receipt_pdf(cv):
    html_string = render_to_string('receipt_pdf/receipt_pdf.html', {'cv': cv})
    html = HTML(string=html_string)
    
    # arquivo temporário para gerar o PDF
    with tempfile.NamedTemporaryFile(delete=True) as output:
        html.write_pdf(target=output.name)
        output.seek(0)
        pdf = output.read()
    
    # cria a resposta HTTP com o PDF
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="curriculo_{cv.full_name}_{cv.id}.pdf"'
    
    return response

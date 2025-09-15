from django.shortcuts import get_object_or_404
from django.views import View
from django.http import HttpResponse
from ..models.cv import CV
from ..services.receipt import generate_receipt_pdf

class ReceiptGenerateView(View):
    def get(self, request, cv_id):
        cv = get_object_or_404(CV, id=cv_id, user=request.user)
        pdf_response = generate_receipt_pdf(cv)
        return pdf_response

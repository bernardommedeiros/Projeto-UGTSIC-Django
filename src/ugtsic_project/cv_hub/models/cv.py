from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings

class CV(models.Model):
    EDUCATION = [
        ('Ensino Médio(Incompleto)', 'Ensino Médio(Incompleto)'),
        ('Ensino Médio(Completo)', 'Ensino Médio(Completo)'),
        ('Ensino Superior(Incompleto)', 'Ensino Superior(Incompleto)'),
        ('Ensino Superior(Completo)', 'Ensino Superior(Completo)'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='candidate_cv')
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    education_level = models.CharField(max_length=30, choices=EDUCATION)
    observations = models.TextField(blank=True, null=True)
    desired_position = models.CharField(max_length=100)
    cv_file = models.FileField(
        upload_to='cvs/',
    )
    ip_address = models.GenericIPAddressField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Currículo"
        verbose_name_plural = "Currículos"
        
    def clean(self):
        errors = {}

        if self.arquivo:
            ext = os.path.splitext(self.cv_file.name)[1].lower()
            valid_extensions = [".doc", ".docx", ".pdf"]
            if ext not in valid_extensions:
                errors["cv_file"] = "Somente cv_files .doc, .docx ou .pdf são permitidos."

            # Validação tamanho (máximo 1MB)
            if self.cv_file.size > 1024 * 1024:  # 1MB
                errors["cv_file"] = "O tamanho máximo permitido é 1MB."

        if errors:
            raise ValidationError(errors)

    def __str__(self):
        return f"{self.user_id.username} - {self.email}"
        
     
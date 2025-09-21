from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class CustomMinimumLengthValidator:
    def __init__(self, min_length=8):
        self.min_length = min_length

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                _(f"A senha deve ter pelo menos {self.min_length} caracteres."),
                code="password_too_short",
            )

    def get_help_text(self):
        return _(f"Sua senha deve ter pelo menos {self.min_length} caracteres.")

class CustomCommonPasswordValidator:
    def validate(self, password, user=None):
        if password.lower() in ["12345678", "senha123", "password"]:
            raise ValidationError(
                _("Essa senha é muito comum, escolha outra."),
                code="password_too_common",
            )

    def get_help_text(self):
        return _("Não use senhas comuns.")

class CustomNumericPasswordValidator:
    def validate(self, password, user=None):
        if password.isdigit():
            raise ValidationError(
                _(" A senha não pode ser composta apenas por números."),
                code="password_entirely_numeric",
            )

    def get_help_text(self):
        return _(" Sua senha não pode ser apenas numérica.")

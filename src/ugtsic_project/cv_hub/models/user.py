from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
import re


class User(AbstractUser):
    avatar_url = models.ImageField(upload_to='users_avatars/', blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name="Usuário"
        verbose_name_plural = "Usuários"
        ordering = ['-username']
    
    def __str__(self):
        return self.username

    def clean(self):
        errors = {}
        
        if self.username and len(self.username) <= 2:
            errors['username'] = "O nome deve possuir no mínimo 3 caracteres"

        if self.username and not re.match(r'^[\w\sÀ-ÿ]+$', self.username):
            errors['username'] = "O nome não pode conter caracteres especiais."
      
        if errors:
            raise ValidationError(errors)


    def save(self, *args, **kwargs):

        self.full_clean()  
        super().save(*args, **kwargs)
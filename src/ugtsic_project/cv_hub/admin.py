from django.contrib import admin
from .models.user import User
from .models.cv import CV
# Register your models here.

admin.site.register(User)
admin.site.register(CV)

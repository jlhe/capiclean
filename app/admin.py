from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(users)
admin.site.register(Servicios)
admin.site.register(roles)
admin.site.register(Servicio_Solicitado)
admin.site.register(Clientes)
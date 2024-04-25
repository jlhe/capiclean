from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
# Modelo usuario
class users(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, null=False, unique=True)
    password = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(default=timezone.now)
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
    def __str__(self):
        return '{}'.format(self.username) 
    
# Modelo Services
class Servicios(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=255, null=False)
    service_description = models.TextField(null=False)
    service_price = models.FloatField(null=False)
    service_qty = models.IntegerField(null=False)
    created_at = models.DateTimeField(default=timezone.now)
    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"  
    def __str__(self):
        return '{}'.format(self.service_name) 
    
# Modelo roles de usuario

class roles(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.ForeignKey(users, on_delete=models.DO_NOTHING, null=True, blank=True)
    # Si True es Admin, False no Admin
    role = models.BooleanField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Role"
        verbose_name_plural = "Roles"
    def __str__(self):
        return '{}'.format(self.role)
    
class Clientes(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=False, unique=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Cliente"
    def __str__(self):
        return '{}'.format(self.email)

class Servicio_Solicitado(models.Model):
    id = models.IntegerField(primary_key=True)
    fecha_solicitud = models.DateTimeField(default=timezone.now)
    servicio = models.ForeignKey(Servicios, on_delete=models.DO_NOTHING)
    cliente_email = models.ForeignKey(Clientes, on_delete=models.DO_NOTHING, to_field='email')
    descripcion = models.TextField(null=False)
    cantidad = models.IntegerField(null=False)
    class Meta:
        verbose_name = "Servicio Solicitado"
        verbose_name_plural = "Servicios Solicitados"

    def __str__(self):
        return 'Cliente: {} - Email: {}'.format(self.cliente_email.name, self.cliente_email.email)
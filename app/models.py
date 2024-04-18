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
    
# Modelo Quote Requests
class quote_requests(models.Model):
    quote_id = models.AutoField(primary_key=True)
    checkboxes = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(default=timezone.now)
    class Meta:
        verbose_name = "Quote Request"
        verbose_name_plural = "Quote Requests"   

    def __str__(self):
        return '{}'.format(self.quote_id) 
# Modelo Services
class services(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=255, null=False)
    service_description = models.TextField(null=False)
    service_price = models.FloatField(null=False)
    service_qty = models.IntegerField(null=False)
    created_at = models.DateTimeField(default=timezone.now)
    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"  
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
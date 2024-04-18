from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(users)
admin.site.register(quote_requests)
admin.site.register(services)
admin.site.register(roles)
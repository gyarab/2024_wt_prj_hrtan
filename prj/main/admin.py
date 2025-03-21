from django.contrib import admin
from .models import Server

class ServerAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "region", "cpu", "cores", "ghz", "storage", "port", "traffic", "price"]

admin.site.register(Server, ServerAdmin)

# Register your models here.

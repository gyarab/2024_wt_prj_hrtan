from django.contrib import admin
from .models import Server, Provider, Cart, User, ServerComment

class ServerAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "region", "cpu", "cores", "ghz", "storage", "port", "traffic", "price"]

class ProviderAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "url"]

class CartAdmin(admin.ModelAdmin):
    list_display = ["id", "server_id:"]

class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]

class ServerCommentAdmin(admin.ModelAdmin):
    list_display = ["id", "text", "server_id", "user_id"]



# Register your models here.
admin.site.register(Server, ServerAdmin)
admin.site.register(Provider, ProviderAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(ServerComment, ServerCommentAdmin)
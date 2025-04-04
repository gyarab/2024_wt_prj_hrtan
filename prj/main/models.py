from django.db import models

class Server(models.Model):
    title = models.CharField(max_length=300, default="")
    region = models.CharField(max_length=20, default="")
    cpu = models.CharField(max_length=20, default="")
    cores = models.IntegerField(null=True, blank=True, default=0)
    ghz = models.IntegerField(null=True, blank=True, default=0)
    storage = models.CharField(max_length=30, default="")
    port = models.IntegerField(null=True, blank=True, default=0)
    traffic = models.IntegerField(null=True, blank=True, default=0)
    price = models.IntegerField(null=True, blank=True, default=0)
    provider_id = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return f'{self.title} {self.region} {self.cpu} {self.cores} {self.ghz} {self.storage} {self.port} {self.traffic} {self.price}'
    
    
class Provider(models.Model):
    title = models.CharField(max_length=100, default="")
    url = models.URLField(max_length=200, default="")

    def __str__(self):
        return f'{self.title} {self.url}'
    

class Cart(models.Model):
    server_id = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return f'{self.server_id}'
    

class User(models.Model):
    name = models.CharField(max_length=50, default="")

    def __str__(self):
        return f'{self.name}'
    

class ServerComment(models.Model):
    text = models.TextField(default="")
    server_id = models.IntegerField(null=True, blank=True, default=0)
    user_id = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return f'{self.text} {self.server_id} {self.user_id}'







# Create your models here.

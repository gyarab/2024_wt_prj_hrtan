from django.db import models

class Server(models.Model):
    title = models.CharField(max_length=300)
    region = models.CharField(max_length=20)
    cpu = models.CharField(max_length=20)
    cores = models.IntegerField(null=True, blank=True)
    ghz = models.IntegerField(null=True, blank=True)
    storage = models.CharField(max_length=30)
    port = models.IntegerField(null=True, blank=True)
    traffic = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return f'{self.title} {self.region} {self.cpu} {self.cores} {self.ghz} {self.storage} {self.port} {self.traffic} {self.price}'



# Create your models here.

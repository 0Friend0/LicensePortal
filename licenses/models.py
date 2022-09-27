from pyexpat import model
from venv import create
from django.db import models
import uuid



class Client(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                            primary_key=True, editable=False)
    name = models.CharField(max_length=250, unique=True)
    admin_poc = models.EmailField(max_length=200)
    created = models.DateField(auto_now_add=True)
    

    def __str__(self) -> str:
        return self.name


class License(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateField(blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                            primary_key=True, editable=False)

    class Meta:
        ordering = ['client']

    @property
    def client_name(self):
        return self.client.name
    
    @property
    def client_id(self):
        return self.client.id

    def __str__(self) -> str:
        return self.name







from django.db import models
from django.utils import timezone

# Create your models here.

class tClient (models.Model):
    NIF=models.CharField(max_length=50, primary_key=True,default=1)
    NOMBRE=models.CharField(max_length=250)
    APELLIDO=models.CharField(max_length=250)
    EDAD=models.IntegerField()

    def __str__(self):
        return self.NIF

class tEye (models.Model):
    NIF=models.ForeignKey(tClient, on_delete=models.CASCADE)
    CONSULTA=models.DateTimeField(default=timezone.now)
    OD_ESFERA=models.DecimalField(max_digits=30,decimal_places=2, default=0)
    OD_CILINDRO=models.DecimalField(max_digits=30,decimal_places=2, default=0)
    OD_ADICION=models.DecimalField(max_digits=30,decimal_places=2, default=0)
    OD_AGUDEZA=models.DecimalField(max_digits=30,decimal_places=2, default=0)
    OI_ESFERA=models.DecimalField(max_digits=30,decimal_places=2, default=0)
    OI_CILINDRO=models.DecimalField(max_digits=30,decimal_places=2, default=0)
    OI_ADICION=models.DecimalField(max_digits=30,decimal_places=2, default=0)
    OI_AGUDEZA=models.DecimalField(max_digits=30,decimal_places=2, default=0)



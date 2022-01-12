from django.db import models

# Create your models here.

class tClient (models.Model):
    NIF=models.CharField(max_length=50)
    NOMBRE=models.CharField(max_length=250)
    APPELIDO=models.CharField(max_length=250)
    EDAD=models.IntegerField()

class tEye (models.Model):
    ID=models.IntegerField()
    NIF=models.CharField(max_length=50)
    CONSULTA=models.DateTimeField()
    OD_ESFERA=models.DecimalField(max_digits=30,decimal_places=15)
    OD_CILINDRO=models.DecimalField(max_digits=30,decimal_places=15)
    OD_ADICION=models.DecimalField(max_digits=30,decimal_places=15)
    OD_AGUDEZA=models.DecimalField(max_digits=30,decimal_places=15)
    OI_ESFERA=models.DecimalField(max_digits=30,decimal_places=15)
    OI_CILINDRO=models.DecimalField(max_digits=30,decimal_places=15)
    OI_ADICION=models.DecimalField(max_digits=30,decimal_places=15)
    OI_AGUDEZA=models.DecimalField(max_digits=30,decimal_places=15)



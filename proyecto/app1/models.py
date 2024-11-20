from django.db import models

# Create your models here.
class Modalidad(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)

    class Meta:
        #Configuramos el nombre con el que se crea la tabla en bd
        db_table = 'modalidad'

    def __str__(self):
        return self.nombre + '-' + self.descripcion   

class Carrera(models.Model):
    nombre = models.CharField(max_length=200)
    codigo = models.CharField(max_length=15)
    modalidad = models.ForeignKey(Modalidad, db_column='modalidad', blank=True, null=True, on_delete=models.SET_NULL)
    #register = models.DateField(auto_now=True)
    class Meta:
        db_table = 'carrera' #app1_carrera

    def __str__(self):
        return self.nombre + '-' + self.modalidad.nombre      

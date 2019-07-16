from urllib.parse import quote

from django.db import models


class Coleccion(models.Model):
    handle = models.CharField(max_length=50)
    idcoleccion = models.AutoField(primary_key=True)
    mensaje_exito = models.CharField(max_length=45)
    mensaje_falla = models.CharField(max_length=45)
    nombre = models.CharField(max_length=45)
    nombre_token = models.CharField(max_length=45)
    prompt = models.CharField(max_length=45)
    respuesta = models.CharField(max_length=45)

    class Meta:
        db_table = 'coleccion'
        managed = False
        verbose_name_plural = "colecciones"

    def __str__(self):
        return "%s" % self.nombre

    def __unicode__(self):
        return u'%s' % self.nombre

    def save(self, *args, **kwargs):
        self.handle = quote(self.nombre.lower())
        super().save(*args, **kwargs)  # Call the "real" save() method.

import os

from django.conf import settings
from django.db import models


def get_file_path(instance, filename):
    if instance.coleccion is None:
        ruta = settings.BASE_STATIC_DIR
    else:
        ruta = os.path.join(settings.BASE_STATIC_DIR, instance.coleccion.nombre, filename)
    return ruta


class Foto(models.Model):
    archivo = models.ImageField(upload_to=get_file_path)
    idfoto = models.AutoField(primary_key=True)
    coleccion = models.ForeignKey('Coleccion', on_delete=models.DO_NOTHING, db_column='idcoleccion')

    class Meta:
        db_table = 'foto'
        managed = False
        verbose_name_plural = "fotos"

    def __str__(self):
        return "%s" % self.archivo

    def __unicode__(self):
        return u'%s' % self.archivo

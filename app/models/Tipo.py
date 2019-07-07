from django.db import models


class Tipo(models.Model):
    BLOG = 2
    idtipo = models.AutoField(primary_key=True)
    LINK = 1
    nombre = models.CharField(max_length=45)

    def __str__(self):
        return "%s" % self.nombre

    def __unicode__(self):
        return u'%s' % self.nombre

    class Meta:
        db_table = 'tipo'
        managed = False
        verbose_name_plural = "tipos"

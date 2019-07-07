from django.db import models
from django.conf import settings


class Foto(models.Model):
    archivo = models.ImageField()
    directorio = models.CharField(max_length=255, default=settings.MEDIA_ROOT, editable=False)
    handle = models.CharField(max_length=255)
    idfoto = models.AutoField(primary_key=True)
    
    class Meta:
        db_table = 'foto'
        managed = False
        verbose_name_plural = "fotos"
    
    def __str__(self):
        return "%s" % self.handle
    
    def __unicode__(self):
        return u'%s' % self.handle

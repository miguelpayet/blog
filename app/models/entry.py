from .tag import Tag
from django.db import models
from django.db.models import Max, Min


class Entry(models.Model):
    cambiado = models.DateTimeField()
    creado = models.DateTimeField()
    descripcion = models.TextField()
    handle = models.CharField(max_length=255)
    identry = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=512)
    
    class Meta:
        db_table = 'entry'
        managed = False
        verbose_name_plural = "entries"
    
    def __str__(self):
        return "%s" % self.titulo
    
    def __unicode__(self):
        return u'%s' % self.titulo
    
    def tags(self):
        tags = Tag.objects.filter(identry=self.identry)
        return list(tags)
    
    @staticmethod
    def ultimo():
        return Entry.objects.latest('creado')
    
    @staticmethod
    def anterior(entry):
        qs = Entry.objects.filter(creado__lt=entry.creado)
        res = qs.aggregate(Max('creado'))
        if res['creado__max'] is None:
            anterior = None
        else:
            latest = Entry.objects.filter(creado=res['creado__max']).order_by("-identry")
            anterior = latest.first()
        return anterior
    
    @staticmethod
    def siguiente(entry):
        qs = Entry.objects.filter(creado__gt=entry.creado)
        res = qs.aggregate(Min('creado'))
        if res['creado__min'] is not None:
            latest = Entry.objects.filter(creado=res['creado__min']).order_by("-identry")
            siguiente = latest.first()
        else:
            siguiente = None
        return siguiente
    
    @staticmethod
    def obtener_slug(slug):
        qs = Entry.objects.filter(handle=slug)
        return qs.first()

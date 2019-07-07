from django.db import models
from django.db.models import Max
from django.db.models import Min

from .Tag import Tag
from .Tipo import Tipo


class Entry(models.Model):
    cambiado = models.DateTimeField(editable=False)
    creado = models.DateTimeField(editable=False)
    descripcion = models.TextField()
    handle = models.CharField(max_length=255)
    identry = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=512)
    tipo = models.ForeignKey('Tipo', on_delete=models.DO_NOTHING, db_column='idtipo')

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
        return Entry.objects.filter(tipo__idtipo=Tipo.BLOG).latest('creado')

    @staticmethod
    def anterior(entry):
        qs = Entry.objects.filter(creado__lt=entry.creado).filter(tipo__idtipo=Tipo.BLOG)
        res = qs.aggregate(Max('creado'))
        if res['creado__max'] is None:
            anterior = None
        else:
            latest = Entry.objects.filter(creado=res['creado__max']).order_by("-identry").filter(tipo__idtipo=Tipo.BLOG)
            anterior = latest.first()
        return anterior

    @staticmethod
    def siguiente(entry):
        qs = Entry.objects.filter(creado__gt=entry.creado).filter(tipo__idtipo=Tipo.BLOG)
        res = qs.aggregate(Min('creado'))
        if res['creado__min'] is not None:
            latest = Entry.objects.filter(creado=res['creado__min']).order_by("-identry").filter(tipo__idtipo=Tipo.BLOG)
            siguiente = latest.first()
        else:
            siguiente = None
        return siguiente

    @staticmethod
    def obtener_slug(slug):
        qs = Entry.objects.filter(handle=slug)
        return qs.first()
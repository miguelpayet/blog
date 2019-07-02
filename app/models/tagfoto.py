from django.db import models


class TagFoto(models.Model):
    idtagfoto = models.AutoField(primary_key=True)
    idfoto = models.ForeignKey('Foto', on_delete=models.CASCADE, db_column='idfoto', )
    tag = models.CharField(max_length=45)

    def __str__(self):
        return "%s" % self.tag

    def __unicode__(self):
        return u'%s' % self.tag

    class Meta:
        db_table = 'tagfoto'
        managed = False
        verbose_name_plural = "tagsfoto"

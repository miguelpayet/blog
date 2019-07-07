from django.db import models


class Tag(models.Model):
    idtag = models.AutoField(primary_key=True)
    identry = models.ForeignKey('Entry', on_delete=models.DO_NOTHING, db_column='identry', )
    tag = models.CharField(max_length=45)
    
    def __str__(self):
        return "%s" % self.tag
    
    def __unicode__(self):
        return u'%s' % self.tag
    
    class Meta:
        db_table = 'tag'
        managed = False
        verbose_name_plural = "tags"

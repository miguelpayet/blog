from django.db import models


class Tag(models.Model):
    idtag = models.AutoField(primary_key=True)
    tag = models.CharField(max_length=45)

    def __str__(self):
        return "%s" % self.tag

    def __unicode__(self):
        return u'%s' % self.tag

    class Meta:
        db_table = 'tag'
        managed = False
        verbose_name_plural = "tags"


class TagEntry(models.Model):
    idtagentry = models.AutoField(primary_key=True)
    entry = models.ForeignKey('Entry', on_delete=models.DO_NOTHING, db_column='identry')
    tag = models.ForeignKey('Tag', on_delete=models.DO_NOTHING, db_column='idtag')

    def __str__(self):
        return 'tag %s - %s' % (self.entry, self.tag)

    def __unicode__(self):
        return u'tag %s - %s' % (self.entry, self.tag)

    class Meta:
        db_table = 'tag_entry'
        managed = False
        verbose_name_plural = "tags"

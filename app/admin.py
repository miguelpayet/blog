# from django.db import models
# from django.forms import Textarea, ModelForm, ChoiceField, RadioSelect
from django.contrib import admin

from app.models import Entry, Tag, TagFoto, Foto


class TagInline(admin.TabularInline):
    model = Tag
    fields = ('tag',)
    extra = 0


class EntryAdmin(admin.ModelAdmin):
    list_display = ('identry', 'titulo', 'tags',)
    inlines = (TagInline,)


admin.site.register(Entry, EntryAdmin)


class TagFotoInline(admin.TabularInline):
    model = TagFoto
    fields = ('tag',)
    extra = 0


class FotoAdmin(admin.ModelAdmin):
    list_display = ('idfoto', 'handle')
    inlines = (TagFotoInline,)


admin.site.register(Foto, FotoAdmin)

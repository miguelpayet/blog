# from django.db import models
# from django.forms import Textarea, ModelForm, ChoiceField, RadioSelect
from app.models import Entry
from django.contrib import admin


class EntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo',)


admin.site.register(Entry, EntryAdmin)

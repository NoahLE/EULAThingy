from django.db import models
from django import forms


class ThingyStrings(models.Model):
    doc_title = models.CharField(
        max_length=250, null=False, blank=False,
        verbose_name='Document title.'
    )
    string_rating = models.IntegerField(
        max_length=1, null=True, blank=False, default=0
    )
    last_modified = models.DateTimeField(
        auto_now_add=True, null=False, blank=False
    )
    uploaded = models.DateTimeField(
        auto_now_add=True, null=False, blank=False
    )


class ThingyDocs(models.Model):
    doc_title = models.ForeignKey(ThingyStrings, db_index=True)

    doc_rating = models.IntegerField(
        max_length=1, null=False, blank=False, default=0
    )
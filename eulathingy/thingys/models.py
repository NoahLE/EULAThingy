from django.db import models


class ThingyDoc(models.Model):
    doc_title = models.CharField(
        max_length=250, null=False, blank=False,
        verbose_name='Document title.'
    )
    doc_rating = models.IntegerField(
        max_length=1, null=False, blank=False, default=0
    )
    doc_votes = models.IntegerField(
        null=False, blank=False, default=0
    )
    doc_company = models.IntegerField(
        max_length=250, null=False, blank=True
    )
    category_choices = (
        (0, 'Other'),
        (1, 'Health'),
        (2, 'Technology'),
        (3, 'Finance'),
        (4, 'Service')
    )
    category = models.IntegerField(
        choices=category_choices, null=False,
        blank=False, db_index=True, default=0
    )
    last_modified = models.DateTimeField(
        auto_now_add=True, null=False, blank=False
    )
    uploaded = models.DateTimeField(
        auto_now_add=True, null=False, blank=False
    )


class ThingyString(models.Model):
    doc = models.ForeignKey(ThingyDoc, db_index=True)

    string = models.CharField(
        max_length=500, null=False, blank=False
    )
    string_rating = models.IntegerField(
        max_length=1, null=True, blank=False, default=0
    )
    string_votes = models.IntegerField(
        null=False, blank=False, default=0
    )
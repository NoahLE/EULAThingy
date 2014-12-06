from django.db import models


class Thingy(models.Model):
    """
    A high-level object to hold information on an upload of a Thingy.

    A Thingy is defined as:
        * terms and conditions
        * EULAs
        * Anything with an enormous amount of text and overly complex
        language.
    """
    name = models.CharField(
        max_length=100, null=False, blank=False
    )
    summary = models.CharField(
        max_length=200, null=True, blank=False
    )
    uploaded_on = models.DateTimeField(
        auto_now_add=True, null=False, blank=False
    )


class ThingySection(models.Model):
    """
    A section of a Thingy's content. Thingys are broken up into sections
    which are then serialised into the DB. The parser will remove data that
    isn't required and attempt to keep only that which is useful.
    """
    section_name = models.CharField(
        max_length=50, null=True, blank=False
    )
    content = models.TextField(
        null=False, blank=False
    )
    thingy = models.ForeignKey(Thingy)

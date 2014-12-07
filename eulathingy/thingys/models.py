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


class ThingySection(models.Model):
    """
    A section of a Thingy's content. Thingys are broken up into sections
    which are then serialised into the DB. The parser will remove data that
    isn't required and attempt to keep only that which is useful.
    """
    thingy = models.ForeignKey(Thingy, db_index=True)
    content = models.TextField(null=False, blank=False)


class ThingySentence(models.Model):
    """

    """
    content = models.TextField(
        null=False, blank=False,
        verbose_name='Sentence content'
    )
    thingy_section = models.ForeignKey(ThingySection, db_index=True)
    rating = models.IntegerField(
        null=False, default=0,
        verbose_name='The rating of this sentence'
    )

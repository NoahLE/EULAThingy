from django import forms
from eulathingy.thingys.models import ThingyString


class ThingyForm(forms.Form):
    class Meta:
        model = ThingyString
        fields = ['string_rating']
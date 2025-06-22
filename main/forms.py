from django import forms
from .models import Murojaat


class MurojaatForm(forms.ModelForm):
    class Meta:
        model = Murojaat
        fields = ("ism","email","phone","matn")

from django import forms
from .models import Csv


class CsvMOdelForm(forms.ModelForm):
    class Meta:
        model = Csv
        fields = ('file_name',)


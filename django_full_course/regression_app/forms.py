from django import forms
import pandas as pd

class CSVUploadForm(forms.Form):
    file = forms.FileField()

class ColumnSelectionForm(forms.Form):
    dependent_column = forms.ChoiceField(choices=[])
    independent_columns = forms.MultipleChoiceField(choices=[], widget=forms.CheckboxSelectMultiple)
    train_test_split = forms.FloatField(initial=0.8, min_value=0.1, max_value=0.9)

    def __init__(self, *args, **kwargs):
        csv_data = kwargs.pop('csv_data', None)
        super(ColumnSelectionForm, self).__init__(*args, **kwargs)
        if csv_data is not None:
            choices = [(col, col) for col in csv_data.columns]
            self.fields['dependent_column'].choices = choices
            self.fields['independent_columns'].choices = choices

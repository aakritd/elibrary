# forms.py
from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label = "",max_length=200, error_messages={'required': ''},widget=forms.TextInput(attrs={'class': 'searchbookform', 'placeholder': 'Search Book'}))



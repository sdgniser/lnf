from django import forms

from .models import *

class SearchForm(forms.Form):
    keyword = forms.CharField(max_length = 200)

from django import forms
from django.forms import ModelForm

from .models import *

DEFAULT_CATEGORIES = [
            (''                 , '--------'         ),
            ('Badminton Racket' , 'Badminton Racket' ),
            ('Bag'              , 'Bag'              ),
            ('Book'             , 'Book'             ),
            ('Charger'          , 'Charger'          ),
            ('Debit/Credit Card', 'Debit/Credit Card'),
            ('Earphones'        , 'Earphones'        ),
            ('Keys'             , 'Keys'             ),
            ('Money'            , 'Money'            ),
            ('Notebook'         , 'Notebook'         ),
            ('Phone'            , 'Phone'            ),
            ('Spectacles'       , 'Spectacles'       ),
            ('Umbrella'         , 'Umbrella'         ),
            ('Wallet'           , 'Wallet'           ),
            ('Water Bottle'     , 'Water Bottle'     ),
            ('Other'            , 'Other'            )
        ]

class SearchForm(forms.Form):
    keyword = forms.CharField(max_length = 200)

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['kind', 'location', 'date', 'category', 'desc', 'image',
                'submitter', 'email']

    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['category'].widget = forms.Select(
            choices=DEFAULT_CATEGORIES
        )

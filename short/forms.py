from django import forms
from .models import Myurl
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions, InlineRadios

class MyurlForm(forms.ModelForm):
    class Meta:
        model = Myurl
        # fields = ('longurl','shorturl', 'desc',)
        fields = ('longurl', 'desc',)

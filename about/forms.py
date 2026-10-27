from django import forms

from .models import CollaborateRequest


class CollaborateForm(forms.ModelForm):
    """
    Provides a form for submitting collaboration requests
    using :model:`about.CollaborateRequest`.
    """

    class Meta:
        model = CollaborateRequest
        fields = ('message', 'email', 'name', )

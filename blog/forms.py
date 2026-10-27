from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Provides a form for submitting comments
    using :model:`blog.Comment`.
    """

    class Meta:
        model = Comment
        fields = ('body',)
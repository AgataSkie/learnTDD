from django import forms
from intro import models


class CommentForm(forms.ModelForm):

    class Meta:
        model = models.Comment
        exclude = []

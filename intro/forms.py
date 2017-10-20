from django import forms
from intro import models


class CommentForm(forms.ModelForm):

    class Meta:
        model = models.Comment
        exclude = []

    def clean_text(self):
        data = self.cleaned_data.get('text')
        if len(data) <= 1:
            raise forms.ValidationError("Your comment is too short")
        return data

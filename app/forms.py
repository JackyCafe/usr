from django import forms

from app.models import Reading


class ReadingForm(forms.ModelForm):
    class Meta:
        model = Reading
        fields = ['title','category','content']
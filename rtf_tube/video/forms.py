from django import forms
from .validators import validate_file_extension

class UploadVideoForm(forms.Form):
    video = forms.FileField(label='Видео', validators=[validate_file_extension])
    description = forms.CharField(label='Описание', max_length=300)

class CommentForm(forms.Form):
    comment = forms.CharField(label='', widget=forms.Textarea(), max_length=100)
from django import forms
from .validators import validate_file_extension

class UploadVideoForm(forms.Form):
    title = forms.CharField(label='Название', max_length=50)
    description = forms.CharField(label='Описание', widget=forms.Textarea(), max_length=300)
    video = forms.FileField(label='Видео', validators=[validate_file_extension])
    preview = forms.FileField(label='Превью', required=False)
    
class CommentForm(forms.Form):
    comment = forms.CharField(label='', widget=forms.Textarea(), max_length=100)
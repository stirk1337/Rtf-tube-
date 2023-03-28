from django import forms
from .validators import validate_file_extension

class UploadVideoForm(forms.Form):
    video = forms.FileField(label='Видео', validators=[validate_file_extension])
    description = forms.CharField(label='Описание', max_length=300, widget=forms.TextInput(attrs={'placeholder': 'Описание'}))

class CommentForm(forms.Form):
    video_id = forms.IntegerField(widget = forms.HiddenInput(),)
    comment = forms.CharField(label='', widget=forms.Textarea(), max_length=100)

class LikeForm(forms.Form):
    video_id = forms.IntegerField(widget = forms.HiddenInput(),)

class DislikeForm(forms.Form):
    video_id = forms.IntegerField(widget = forms.HiddenInput(),)
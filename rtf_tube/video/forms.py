from django import forms
from .validators import validate_video_extension, validate_image_extension, file_size

class UploadVideoForm(forms.Form):
    video = forms.FileField(label='Видео', validators=[validate_video_extension, file_size])
    preview = forms.ImageField(label='Превью', validators=[validate_image_extension, file_size], required=False)
    description = forms.CharField(label='Описание', max_length=300, widget=forms.TextInput(attrs={'placeholder': 'Описание'}), required=False)

class CommentForm(forms.Form):
    video_id = forms.IntegerField(widget = forms.HiddenInput(),)
    comment = forms.CharField(label='', widget=forms.Textarea(), max_length=100)

class LikeForm(forms.Form):
    video_id = forms.IntegerField(widget = forms.HiddenInput(),)

class DislikeForm(forms.Form):
    video_id = forms.IntegerField(widget = forms.HiddenInput(),)
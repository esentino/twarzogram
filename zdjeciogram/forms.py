from django.forms import ModelForm

from zdjeciogram.models import Photo


class AddPhotoForm(ModelForm):
    class Meta:
        model=Photo
        fields=['path', 'description']

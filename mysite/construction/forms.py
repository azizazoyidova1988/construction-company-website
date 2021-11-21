from django import forms
from .models import Video,For_Query,Comments


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ["name", "video"]

class For_QueryForm(forms.ModelForm):
    class Meta:
        model = For_Query
        fields = "__all__"

class CommenterForm(forms.ModelForm):
    class Meta:
        model = Comments()
        fields = '__all__'
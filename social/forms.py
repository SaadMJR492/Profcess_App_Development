from django import forms
from .models import PostComment

class CommentForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(attrs={'class': 'form-control-sm', 'placeholder': 'Type the Comment!!!!', 'rows': '2', 'cols': '48'}))
    class Meta:
        model=PostComment
        fields={'content',}

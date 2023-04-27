from .models import Review, Comment
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'content', 'movie', 'image',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
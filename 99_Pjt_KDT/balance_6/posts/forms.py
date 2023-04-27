from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    title = forms.CharField(
         label='', 
         label_suffix='', 
         widget=forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'autofocus': True,
                    'placeholder':"상황 설명(필수)",
                }
            )
        )
    select1_content = forms.CharField(
         label='', 
         label_suffix='', 
         widget=forms.Textarea(
                attrs={
                    'class': 'form-control text-wrap custom-select-form', 
                    'autofocus': True,
                    'placeholder':"선택지1(필수)",
                }
            )
        )
    select2_content = forms.CharField(
         label='', 
         label_suffix='', 
         widget=forms.Textarea(
                attrs={
                    'class': 'form-control text-wrap custom-select-form', 
                    'autofocus': True,
                    'placeholder':"선택지2(필수)",
                }
            )
        )
    img1 = forms.ImageField(
        label='', 
        label_suffix='',
        required=False,
        )
    img2 = forms.ImageField(
        label='', 
        label_suffix='',
        required=False,
        )
    class Meta:
        model = Post
        fields = ('title', 'select1_content', 'select2_content', 'img1', 'img2',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
    
    content = forms.CharField(
        label='댓글',
        label_suffix='',
        widget=forms.Textarea(
            attrs={
                'placeholder': '댓글을 작성주세요.',
                "class": "form-control",
                'style': 'width: 100%; height: 3rem;',   
            }
        ),
    )
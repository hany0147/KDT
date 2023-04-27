from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    title = forms.CharField(
                label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': '제목을 입력해주세요.',
            },
        ),
    )
    content = forms.CharField(
                label='내용',
        widget=forms.Textarea(
            attrs={'class': 'my-content' ,
            },
        ),
    )

    CHOICES = (('개발' , '개발'), ('CS', 'CS'), ('신기술', '신기술'))
    category = forms.ChoiceField(
        choices=CHOICES,
    )

    class Meta:
        model = Post
        fields = '__all__'









from django import forms

from .models import Post, Comment
from products.widgets import CustomClearableFileInput


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'blog_content', 'status', 'image',)

    image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInput)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('comment_content',)

    def __init__(self, *args, **kwargs):
        """ Add placeholder and remove auto-generated labels """
        super().__init__(*args, **kwargs)
        placeholders = {
            'comment_content': 'Add Comment',
        }

        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-1'
            self.fields[field].label = False

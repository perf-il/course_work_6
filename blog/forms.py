from django import forms
from blog.models import Blog


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })


class BlogForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('title_name', 'content', 'preview', )
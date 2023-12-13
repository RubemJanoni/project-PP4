from django import forms
from blog.models import Post


class Publication_form(forms.ModelForm):    

    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['title', 'author', 'featured_image', 'content', 'status']

    featured_image = forms.ImageField(label='Upload Image')



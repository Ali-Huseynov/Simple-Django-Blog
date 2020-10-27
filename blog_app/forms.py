from django import forms
from .models import Post , Comments



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','category','body']

        widgets = {

            #'author': forms.Select(attrs={  'style':'max-width: 24rem;'}),
            'category' : forms.Select(attrs={'style':'max-width: 24rem;'}),
            'title': forms.TextInput(attrs={ 'style':'max-width: 24rem;'}),
            'body': forms.Textarea(attrs={'style':'height: 12rem; max-height: 12rem; min-height: 12rem; '}),

        }


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post

        fields = ['title','category','body']

        widgets = {
            'title': forms.TextInput(attrs={ 'style':'max-width: 24rem;' }),
            'category' : forms.Select(attrs={'style':'max-width: 24rem;'}),
            'body' : forms.Textarea(attrs= {'style':'height: 12rem; max-height: 12rem; min-height: 12rem; '}),

        }


class CreateCommentForm(forms.ModelForm):

    class Meta:
        model = Comments

        fields = ['body']

        widgets = {
            'body' : forms.Textarea( attrs={ 'style': 'max-width:600px; max-height : 120px ; resize: none; margin-top:5px; ' , 'placeholder':'Enter your comment...' } )

        }
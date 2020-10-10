from django import forms

from .models import Comment
class Comments(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('post','content')
        widgets={

        'post' : forms.Select(attrs={'class':'form-control' ,'placeholder':' Name'}),
        
        'content' : forms.Textarea(attrs={'class':'form-control' , 'rows' : 3 ,'placeholder':'create your comment here'}),


        }
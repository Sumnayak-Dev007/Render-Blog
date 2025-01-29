from django import forms
from .models import UserPost,Comments

class PostForm(forms.ModelForm):
    class Meta:
        model = UserPost
        fields = ['title','content','image']

class CommentForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Write Your Thoughts on This Blog','class':'mt-2 focus:ring-1 focus:ring-blue-500'}))
    
    class Meta:
        model = Comments
        fields = ['content']
        
from django import forms
from .models import UserPost,Comments,Contact,Catblog

class PostForm(forms.ModelForm):
    class Meta:
        model = UserPost
        fields = ['title','content','image']

class CommentForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Write Your Thoughts on This Blog','class':'mt-2 focus:ring-1 focus:ring-blue-500'}))
    
    class Meta:
        model = Comments
        fields = ['content']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['subject','message']

class CatblogForm(forms.ModelForm):
    class Meta:
        model = Catblog
        fields = ['category','slug',
                  'title','blog_image','small_description','descriptions',
                  'tag','meta_title','meta_keywords']
        labels = {
            'slug': 'Unique Name',  
            'meta_title': 'Search Title',  
            'meta_keywords': 'Search Keywords'
        }
        
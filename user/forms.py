from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class EditProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']

    def __init__(self, *args, **kwargs):
        super(EditProfile, self).__init__(*args, **kwargs)
        
        for fieldname in ['username', 'email']:
                self.fields[fieldname].help_text = None

class EditPro(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio','pic']

        widgets = {
                'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Write about yourself...'}),
                'pic': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            }
    
    def __init__(self, *args, **kwargs):
        super(EditPro, self).__init__(*args, **kwargs)
        
        for fieldname in ['bio', 'pic']:
                self.fields[fieldname].help_text = None

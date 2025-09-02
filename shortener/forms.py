from django import forms
from .models import URL

class URLForm(forms.ModelForm):
    class Meta:
        model = URL
        fields = ['original_url']
        widgets = {
            'original_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a valid URL like https://example.com'
            }),
        }

    def clean_original_url(self):
        url = self.cleaned_data['original_url']
        if not url.startswith('http://') and not url.startswith('https://'):
            raise forms.ValidationError("URL must start with http:// or https://")
        return url

from django import forms
from .models import Post, Stock

MAX_POST = 1000000
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']
    
    def content_length_check(self):
        content = self.cleaned_data.get('content')
        if len(content) > MAX_POST:
            raise forms.ValidationError("Sorry, we can't handle more than a million characters")
        return content

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ["ticker"]
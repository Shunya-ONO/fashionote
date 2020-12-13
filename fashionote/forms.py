from django import forms
from .models import Brand
from taggit.forms import TagWidget
from django.forms import TextInput, Textarea, FileInput

class BrandForm(forms.ModelForm):

    class Meta:
        model = Brand
        fields = ('brand_name', 'concept', 'url', 'memo', 'image', 'tags')
        labels = {'brand_name':'ブランド名', 'concept':'コンセプト', 'url':'URL', 'memo':'その他の情報', 'image':'画像を添付', 'tags':'タグ'}
        widgets = { 
      'brand_name': TextInput(attrs={'placeholder': 'ブランド名'}),
      'concept': Textarea(attrs={'placeholder': 'ブランドコンセプト'}),
      'url': TextInput(attrs={'placeholder': 'URL'}),
      'memo': Textarea(attrs={'placeholder': 'そのほかの情報'}),
      'tags': TagWidget(attrs={'placeholder': 'タグ ,で区切ってください'}), 
     } 

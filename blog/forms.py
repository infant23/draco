from django import forms
from django.core.exceptions import ValidationError
from tinymce import TinyMCE
from .tinymce_config import TINYMCE_POST_CONFIG, TINYMCE_COMMENT_CONFIG 

from .models import Category, Post, Tag, Comment

class CommentForm(forms.ModelForm):

	class Meta:
		model = Comment
		fields = ['name', 'email', 'content']

		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'email': forms.TextInput(attrs={'class': 'form-control'}),
			'content': TinyMCE(attrs={'class': 'form-control'}, mce_attrs=TINYMCE_COMMENT_CONFIG),
		}

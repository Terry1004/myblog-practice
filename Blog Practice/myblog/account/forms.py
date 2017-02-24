from django import forms
from .models import Blog, Comment
from django.core.validators import MaxLengthValidator

class CreateBlogForm(forms.Form):

	max_length_validator = MaxLengthValidator(
		limit_value = 1000,
		message = 'You have exceeded the maximum length')
	blog_content = forms.CharField(
		max_length = 1000, 
		validators = [max_length_validator], 
		widget = forms.Textarea(attrs = {
			'class': 'form-control',
			'name': 'blog-content',
			'placeholder': 'Share your moments here...'
			}))


class CreateCommentForm(forms.Form):

	max_length_validator = MaxLengthValidator(
		limit_value = 1000,
		message = 'You have exceeded the maximum length')
	comment_content = forms.CharField(
		max_length = 1000,
		validators = [max_length_validator],
		widget = forms.Textarea(attrs = {
			'class': 'form-control',
			'name': 'comment-content',
			'placeholder': 'add a comment'
			}))
	

class EditProfileForm(forms.Form):

	avatar = forms.ImageField()


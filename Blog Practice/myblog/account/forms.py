from django import forms
from .models import Blog, Comment
from django.core.validators import MaxLengthValidator

class CreateBlogForm(forms.Form):

	max_length_validator = MaxLengthValidator(
		limit_value = 140,
		message = 'You have exceeded the maximum length')
	blog_content = forms.CharField(
		max_length = 140, 
		validators = [max_length_validator], 
		widget = forms.Textarea)


class CreateCommentForm(forms.Form):

	max_length_validator = MaxLengthValidator(
		limit_value = 50,
		message = 'You have exceeded the maximum length')
	comment_content = forms.CharField(
		max_length = 50,
		validators = [max_length_validator],
		widget = forms.Textarea)
	

class EditProfileForm(forms.Form):

	avatar = forms.ImageField()


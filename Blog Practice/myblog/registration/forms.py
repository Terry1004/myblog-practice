from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
import re

class RegistrationForm(forms.Form):

	username = forms.CharField(
		label = 'Username', 
		max_length = 20,  
		widget = forms.TextInput(attrs = {
			'class': 'form-control',
			'placeholder': 'Username'
			}))
	password = forms.CharField(
		label = 'Password', 
		max_length = 20, 
		widget = forms.PasswordInput(attrs = {
			'class': 'form-control',
			'placeholder': 'Password'
			}))
	confirm_password = forms.CharField(
		label = 'Confirm your password', 
		max_length = 20, 
		widget = forms.PasswordInput(attrs = {
			'class': 'form-control',
			'placeholder': 'Confirm password'
		}))

	def clean(self):
		cleaned_data = super(RegistrationForm, self).clean()
		user_name = cleaned_data.get('username')
		password1 = cleaned_data.get('password')
		password2 = cleaned_data.get('confirm_password')
		try:
			user = User.objects.get(username = user_name)
		except User.DoesNotExist:
			pass
		else:
			if (user is not None):
				raise forms.ValidationError(_('The username has been registered.'), code = 'duplicate_username')
		finally:
			pattern = re.compile('^([\w]+)$')
			if (not pattern.match(user_name)):
				raise forms.ValidationError(_('Username should only contain alphanumeric character and the underscore.'), code = 'invalid_username')
			elif (password1 != password2):
				raise forms.ValidationError(_('You have entered different passwords.'), code = 'inequal_password')
			return cleaned_data

from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.core.validators import RegexValidator

class RegistrationForm(forms.Form):
	username_validator = RegexValidator(
		regex = r'^[\w]+$', 
		message = 'Username should only contain alphanumeric character and the underscore.', 
		code = 'invalid_username')
	username = forms.CharField(label = 'Username', max_length = 20, validators = [username_validator])
	password = forms.CharField(label = 'Password', max_length = 20, widget = forms.PasswordInput)
	confirm_password = forms.CharField(label = 'Confirm your password', max_length = 20, widget = forms.PasswordInput)

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
				error = forms.ValidationError(_('The username has been registered.'), code = 'duplicate_username')
				self.add_error('username', error)
		finally:
			if (password1 != password2):
				error = forms.ValidationError(_('You have entered different passwords.'), code = 'inequal_password')
				self.add_error('password', error)
			return cleaned_data

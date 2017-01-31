from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from account.models import Profile
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

# Create your views here.

class RegisterView(FormView):
	template_name = 'registration/register.html'
	form_class = RegistrationForm
	success_url = reverse_lazy('account:dashboard')
	def form_valid(self, form):
		user = User.objects.create_user(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
		profile = Profile.objects.create(user = user)
		user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
		login(self.request, user)
		return super(RegisterView, self).form_valid(form)


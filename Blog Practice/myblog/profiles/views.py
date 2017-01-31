from django.shortcuts import render
from django.contrib.auth.models import User
from account.models import Profile
from django.http import Http404, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate
from django.urls import reverse_lazy
import json
import django

# Create your views here.
def public_profile(request, username):
	def is_following():
		if (current_user.is_authenticated()):
			try:
				profile.followed.get(user = current_user)
			except (Profile.DoesNotExist):
				return False
			else:
				return True
		else:
			return False

	def get_context_data():
		context = {}
		context['username'] = username
		context['profile'] = profile
		context['blogs'] = profile.blog_set.all().order_by('-blog_pub_date')
		context['following'] = profile.follow.all()
		context['followed'] = profile.followed.all()
		context['current_user'] = current_user
		if (is_following()):
			context['follow_change_to'] = '- Unfollow' 
		else:
			context['follow_change_to'] = '+ Follow'
		return context

	current_user = request.user
	try:
		user = User.objects.get(username = username)
	except User.DoesNotExist:
		raise Http404('%s does not exist!' % username)
	else:
		profile = user.profile
	if (current_user == profile.user):
		return HttpResponseRedirect(reverse_lazy('account:profile'))
	else:
		return render(request, 'profiles/public_profile.html', get_context_data())

def toggle_follow(request, username):
	response = {'current_follow_status': 'NA'}
	current_user = request.user
	if (current_user.is_authenticated()):
		request_data = request.GET
		follow_change_to = request_data.get('follow_change_to')
		print(follow_change_to)
		user = User.objects.get(username = username)
		if (follow_change_to == '+ Follow'):
			current_user.profile.follow.add(user.profile)
			response['current_follow_status'] = 'following'
		else:
			current_user.profile.follow.remove(user.profile)
			response['current_follow_status'] = 'not following'
	return JsonResponse(response)
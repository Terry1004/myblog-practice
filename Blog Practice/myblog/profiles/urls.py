from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^(?P<username>[\w]+)/$', views.public_profile, name = 'public_profile'),
	url(r'^(?P<username>[\w]+)/ajax/toggle-follow/$', views.toggle_follow, name = 'toggle-follow')
]
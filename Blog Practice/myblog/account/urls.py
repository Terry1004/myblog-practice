from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^profile/$', views.profile, name = 'profile'),
	url(r'^dashboard/$', views.dashboard, name = 'dashboard'),
	url(r'^blog-edit/(?P<blog_id>[0-9]+)/$', views.edit_blog, name = 'edit_blog'),
	url(r'^dashboard/ajax/delete-blog/$', views.delete_blog, name = 'delete_blog'),
	url(r'^dashboard/ajax/like-blog/$', views.like_blog, name = 'like_blog'),
	url(r'^dashboard/ajax/add-comment/$', views.add_comment, name = 'add_comment'),
	url(r'^dashboard/comment-form/$', views.load_comment_form, name = 'load_comment_form'),
	url(r'^dashboard/comment-reply-form/$', views.load_comment_reply_form, name = 'load_comment_reply_form'),
	url(r'^dashboard/ajax/delete-comment/$', views.delete_comment, name = 'delete_comment'),
	url(r'^profile-edit/$', views.edit_profile, name = 'edit_profile')
]
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseForbidden, JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Profile, Blog, Comment
from .forms import CreateBlogForm, CreateCommentForm
from django.db.models import Q

# Create your views here.
@login_required
def profile(request):
	user = request.user
	user_profile = user.profile
	def get_context_data():
		user_following_list = user_profile.follow.all()
		user_followed_list = user_profile.followed.all()
		blogs = Blog.objects.filter(blog_author = user_profile).order_by('-blog_pub_date')[:5]
		context = {}
		context['blogs'] = blogs
		context['profile'] = user_profile
		context['following'] = user_following_list
		context['followed'] = user_followed_list
		return context

	return render(request, 'account/profile.html', get_context_data())


@login_required
def dashboard(request):
	user = request.user
	user_profile = user.profile
	def get_context_data():
		user_following_list = user_profile.follow.all()
		blogs = Blog.objects.filter(Q(blog_author__in = user_following_list) | Q(blog_author = user_profile)).order_by('-blog_pub_date')[:5]
		context = {}
		context['blogs'] = blogs
		context['profile'] = user_profile
		return context

	if (request.method == 'POST'):
		form = CreateBlogForm(request.POST)
		if (form.is_valid()):
			blog_content = form.cleaned_data['blog_content']
			Blog.objects.create(blog_content = blog_content, blog_author = user_profile)
			return HttpResponseRedirect(reverse_lazy('account:dashboard'))
		else:
			context = get_context_data()
			context['blog_form'] = form
			return render(request, 'account/dashboard.html', context)
	else:
		form = CreateBlogForm()
		context = get_context_data()
		context['blog_form'] = form
		return render(request, 'account/dashboard.html', context)


#this view is for displaying the content of corresponding blog and let the user edit it and post again
@login_required
def edit_blog(request, blog_id):
	user = request.user
	user_profile = user.profile
	current_blog = get_object_or_404(Blog, pk = blog_id)

	if (current_blog.blog_author != user_profile):
		return HttpResponseForbidden()
	else:
		context = {'blog_id': blog_id}
		if (request.method != 'POST'):
			form = CreateBlogForm(initial = {'blog_content': current_blog.content})
			context['form'] = form
			return render(request, 'account/edit_blog.html', context)
		else:
			form = CreateBlogForm(request.POST)
			if(form.is_valid()):
				current_blog.content = form.cleaned_data['blog_content']
				current_blog.save()
				return HttpResponseRedirect(reverse_lazy('account:dashboard'))
			else:
				context['form'] = form
				return render(request, 'account/edit_blog.html', context)


#this view is for the user to delete the selected blog
@login_required
def delete_blog(request):
	user = request.user
	user_profile = user.profile
	request_data = request.GET
	blog_id = request_data.get("blog_id")
	response = {}
	try:
		blog = Blog.objects.get(pk = blog_id)
	except Blog.DoesNotExist:
		response['status'] = 'blog not exist'
	else:
		if (user_profile != blog.blog_author):
			response['status'] = 'unauthorized'
		else:
			blog.delete()
			response['status'] = 'successful'
	return JsonResponse(response)


@login_required
def like_blog(request):
	user = request.user
	user_profile = user.profile
	request_data = request.GET
	blog_id = request_data.get("blogId")
	response = {}
	try:
		blog = Blog.objects.get(pk = blog_id)
	except Blog.DoesNotExist:
		response['status'] = 'blog not exist'
	else:
		if (user_profile in blog.like_people.all()):
			blog.like_people.remove(user_profile)
			response['status'] = 'unlike'
		else:
			blog.like_people.add(user_profile)
			response['status'] = 'like'
	return JsonResponse(response)


@login_required
def add_comment(request):
	if (request.method == 'POST'):
		user = request.user
		user_profile = user.profile
		request_data = request.POST
		response = {}
		if (request_data.get('replyTo') == 'None'):
			content = request_data.get('commentContent')
			blog_id = request_data.get('blogId')
			Comment.objects.create(
				comment_content = content,
				comment_author = user_profile,
				blog = Blog.objects.get(pk = blog_id)
				)
			response['status'] = 'successful'
		else:
			reply_to = request_data.get('replyTo')
			content = request_data.get('commentContent')
			Comment.objects.create(
				comment_content = content,
				comment_author = user_profile,
				blog = Comment.objects.get(pk = reply_to).blog,
				reply_to = Comment.objects.get(pk = reply_to)
				)
			response['status'] = 'successful'
		return JsonResponse(response)
	else:
		return HttpResponseForbidden()

@login_required
def load_comment_form(request):
	context = {}
	context['comment_form'] = CreateCommentForm()
	return render(request, 'account/comment_form_snippet.html', context)


@login_required
def load_comment_reply_form(request):
	context = {}
	context['comment_reply_form'] = CreateCommentForm()
	return render(request, 'account/comment_reply_form_snippet.html', context)


@login_required
def delete_comment(request):
	user = request.user
	user_profile = user.profile
	request_data = request.GET
	comment_id = request_data.get('commentId')
	response = {}
	try:
		comment = Comment.objects.get(pk = comment_id)
	except Comment.DoesNotExist:
		response['status'] = 'comment not exist'
	else:
		if (comment.comment_author == user_profile):
			comment.delete()
			response['status'] = 'successful'
		else:
			response['status'] = 'unauthorized'
	return JsonResponse(response)




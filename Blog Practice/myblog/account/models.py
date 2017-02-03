from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
	def get_user_avatar_folder(instance, filename):
		return "avatars/%s/%s" %(instance.user.username, filename)

	user = models.OneToOneField(User, on_delete = models.CASCADE)
	follow = models.ManyToManyField('self', symmetrical = False, related_name = 'followed')
	avatar = models.ImageField(upload_to = get_user_avatar_folder, default = 'avatars/default-avatar.png')


class Blog(models.Model):
	blog_content = models.TextField(max_length = 140)
	blog_pub_date = models.DateTimeField(auto_now = True)
	like_people = models.ManyToManyField(Profile, related_name = 'like_blogs')
	blog_author = models.ForeignKey(Profile, on_delete = models.CASCADE)

class Comment(models.Model):
	comment_content = models.TextField(max_length = 140)
	comment_pub_date = models.DateTimeField(auto_now = True)
	comment_author = models.ForeignKey(Profile, on_delete = models.CASCADE)
	blog = models.ForeignKey(Blog, on_delete = models.CASCADE, related_name = 'comments')
	reply_to = models.ForeignKey('self', related_name = 'replies', on_delete = models.CASCADE, blank=True, null=True)
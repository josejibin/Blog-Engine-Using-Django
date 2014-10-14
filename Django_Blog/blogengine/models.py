from django.db import models
#from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
	user_name = models.CharField(max_length = 200)
	email = models.EmailField()
	password = models.CharField(max_length = 6)

	def __unicode__(self):
		return self.user_name

class Post(models.Model):
    title = models.CharField(max_length=200)
    #catogary = models.CharField(max_length = 50)
    pub_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    slug = models.SlugField(max_length=40, unique=True)
    author = models.ForeignKey(User)

    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
    	return "/%s/%s/%s/" % (self.pub_date.year, self.pub_date.month, self.slug)
    def get_post_id(self,post_slug):
    	pid = self.objects.get(slug = post_slug)
    	return pid


class Comment(models.Model):
	commentor = models.CharField(max_length = 200)
	comment_text = models.TextField()
	comment_date = models.DateTimeField(auto_now_add=True)
	comment_for = models.ForeignKey(Post)

	def __unicode__(self):
		return self.comment_text
	



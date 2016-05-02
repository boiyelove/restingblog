from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save
from django.utils.text import slugify

# Create your models here.

def get_setinel_user():
	return get_user_model().objects.get_or_create(username = 'deleted_User')[0]

class Post(models.Model):
	title = models.CharField(max_length = 30)
	content = models. TextField()
	slug = models.SlugField(unique = True)
	tags = models.ManyToManyField('Tag')
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = get_setinel_user)


class Tag(models.Model):
	name = models.CharField(max_length = 15)
	slug = models.SlugField(unique = True)
	active = models.BooleanField(default = True)


def create_slug(instance, new_slug=None):
	slug = sluggify(instance.title)
	if new_slug  is not None:
		slug = new_slug
	qs = Post.bjects.filter(slug=slug).order_by('-id')
	exists = qs.exists()
	if exists:
		new_slug = '&s-%s' %(slug. qs.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)


	pre_save.connect(pre_save_post_receiver, sender=Post)
	pre_save.connect(pre_save_post_receiver, sender=Tag)
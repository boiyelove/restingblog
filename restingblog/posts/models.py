from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse_lazy
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.
def get_sentinnel_user():
	return get_user_model.objects.get_or_create(username="deleted")[0]

class Timestamp(models.Model):
	created_on = models.DateTimeField(auto_now = True)
	updated_on = models.DateTimeField(auto_now_add = True)
	published_date = models.DateTimeField(blank=True, null=True)
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.SET(get_sentinnel_user))
	class Meta:
		abstract = True

	def publish(self):
		self.published_date = timezone.now()
		self.save()

class Musthave(Timestamp):
	title = models.CharField(max_length = 80, unique=True)
	slug = models.SlugField(unique = True)
	class Meta:
		abstract = True

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.name)
			super(Category, self).save(*args, **kwargs)


class Tag(Musthave):

	def get_absolute_url(self):
			return reverse_lazy('blog:blog_tag_view', kwargs={'slug': self.slug})

class Category(Musthave):
	parent = models.ForeignKey('self', null=True, blank=True)
	description = models.CharField(max_length = 60, null=True, blank = True)

	class Meta:
		verbose_name_plural = "categories"

	def get_subcategories(self):
		return self.objects.filter(
			parent_category__id=target_category.id)

	def get_parent(self):
		if self.parent is not None:
			return self.parent
		else:
			return None

	def get_absolute_url(self):
		return reverse_lazy('blog:blog_category', kwargs={'slug': self.slug})

class Post(Musthave):
	tagline = models.CharField(max_length = 100)
	category = models.ForeignKey('Category', null=True, blank=True)
	content = models.TextField()
	tags = models.ManyToManyField('Tag', blank=True)

	def get_absolute_url(self):
		return reverse_lazy('blog:blog_post_view', kwargs={'slug': self.slug})

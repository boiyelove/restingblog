from django.contrib import admin
from .forms import PostForm
from .models import Post, Category, Tag
# Register your models here.

class PostAdmin(admin.ModelAdmin):
	form = PostForm


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
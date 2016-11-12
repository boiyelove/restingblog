from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	tags = forms.CharField(max_length='80', help_text = "Enter a maximum of 5 tags separated by ','")

	class Meta:
		model = Post
		fields = ('title', 'tagline', 'category', 'content')

	def __init__(self, *args, **kwargs):
		if kwargs.get('instance'):
			initial = kwargs.setdefault('initial', {})
			initial['tags'] += [item + ',' for item in kwargs['instance'].tags_set.all()]
		forms.ModelForm.__init__(self, *args, **kwargs)


	def clean_tags(self):
		tags = self.cleaned_data['tags']
		tags = tags.split(',')
		if len(tags) > 8:
			raise forms.Validation('You can only enter a maximum of 8 tags')
		return tags

	def save(self, commit = True):
		instance = forms.ModelForm.save(self, False)
		old_save_m2m = self.old_save_m2m
		def save_m2m():
			old_save_m2m()
			instance.tags_set.clear()
			tags = self.cleaned_data['tags']
			for tag in tags.split(','):
				thistag, created = Tag.objects.get_or_create(title = tag)
				instance.tags_set.add(thistag)
		self.save_m2m = save_m2m
		if commit:
		 	instance.save()
		 	self.savem2m()
		return instance



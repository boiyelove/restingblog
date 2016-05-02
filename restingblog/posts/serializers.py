#import the models to be srialized
from django.contrib.auth.models import User, Group
from .models import Post, Tag
#import serializer from rest_framework
from rest_framework import serializers


#creating a serializer class
"""
Hyperlinking our API
Dealing with relationships between entities is one of the 
more challenging aspects of Web API design. 
There are a number of different ways that we might 
choose to represent a relationship:

Using primary keys.
Using hyperlinking between entities.
Using a unique identifying slug field on the related entity.
Using the default string representation of the related entity.
Nesting the related entity inside the parent representation.
Some other custom representation.
REST framework supports all of these styles,
 and can apply them across forward or reverse relationships, 
 or apply them across custom managers such as generic foreign keys.

In this case we'd like to use a hyperlinked style between entities.
 In order to do so, we'll modify our serializers to extend HyperlinkedModelSerializer
  instead of the existing ModelSerializer.

The HyperlinkedModelSerializer has the following differences from ModelSerializer:

It does not include the pk field by default.
It includes a url field, using HyperlinkedIdentityField.
Relationships use HyperlinkedRelatedField, instead of PrimaryKeyRelatedField.
"""

class TagSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Tag
		fields = ('title', 'slug', 'active')

class PostSerializer(serializers.HyperlinkedModelSerializer):
	author = serializers.ReadOnlyField(source='author.username')

	class Meta:
		model = Post
		fields = ('title', 'content', 'tags', 'author' )


class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		field = ('url', 'name')

class UserSerializer(serializers.ModelSerializer):
	posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())
	class Meta:
		model = User
		fields = ('id', 'username', 'email', 'groups', 'post')
"""
Notice that we are using hyperlinked relations in the case with HyperlinkedModelSrializer. 
You can also use primary key and various other relationships but hyperlinking is good RESTful design

class PostSerializer1(serializers.Serializer):
	pk = serializers.IntegerField(read_only = True)
	title = serializers.CharField()
	content = serializers.CharField()
	author = serializers.ReadOnlyField(source='author.username')


	def create(self, validated_data):
		'''
		Create and return a new post instance, given the validated data.

		'''
		return Post.objects.create(**validated_data)

	def update(self, instance, validated_data):
		'''
		Update and return an existing Post instance, given the validated_data.
		'''
		instance.title = validated_data.get('title', instance.title)
		instance.content -= validated_data.get('content', instance.content)

		instance.save()
		return instance 
"""
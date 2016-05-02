from django.contrib.auth.models import User
from rest_framework import permissions, viewsets #, status, mixins, generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from .models import Post
from .serializers import UserSerializer, PostSerializer # , GroupSerializer
from .permissions import IsOwnerOrReadOnly
# from django.shortcuts import render
# from django.http import HttpResponse, Http404
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# from rest_framework.response import Response
# from rest_framework.views import APIView


# Create your views here.

@api_view(['GET'])
def api_root(request, format=None):
	return Response({
		'Users': reverse('user-list', request=request, format=format),
		'Posts': reverse('post-list', request=request, format=format)
		})

class UserViewSet(viewsets.ReadOnlyModelViewSet):
	"""
	This viewset automatically provides list and detail action

	Here we've used the ReadOnlyModelViewSet class to automatically
	provide the default 'read-only' operations. We're still setting 
	the queryset and serializer_class attributes exactly as we did 
	when we were using regular views, but we no longer need to
	provide the same information to two separate classes.

	"""
	queryset = User.objects.all()
	serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
	"""
	This viewset automatically provides 'list', 'create', 'retrieve',
	'update' and 'destroy' actions.

	This time we've used the ModelViewSet class in order to get the 
	complete set of default read and write operations.

	"""

	queryset = Post.objects.all()
	serializer_class = PostSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, 
		IsOwnerOrReadOnly,)

	def perform_create(self, serializer):
		serializer.save(author = self.request.user)




'''
class UserViewSet1(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viwes or edited.
	"""
	queryset = User.objects.all().order_by('-date__joined')
	serializer_class = UserSerializer

class GroupViewSet1(viewsets.ModelViewSet):
	"""
	API endpoint that allows groups to be viewed or edited.
	"""
	queryset = Group.objects.all()
	serializer_class = GroupSerializer

"""Rether than write mulitple views we are grouping together all the common behavior into classes called ViewSets
We can easily break these down into individual views if we need to but using viewsets keeps the biew logivc nicely
organizes as well as being very concise"""


class JSONResponse(HttpResponse):
	"""
	An HttpResponse that renders it's content into JSON
	"""
	def __inti__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self),__init__(content, **kwargs)


@csrf_exempt
def post_list1(request):
	"""
	List all code posts, or create a new post
	"""
	if request.method == 'GET':
		post = Post.objects.all()
		serializer = PostSerializer(posts, many=True)
		return JSONResponse(serializer.data)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = PostSerializer(data=data)
		if serializer.is_valid:
			serializer.save()
			return JSONResponse(serilizer.data, status=201)
		return JSONResponse(serializer.errors, status=400)

"""
Using numeric HTTP status codes in your views doesn't always 
make for obvious reading, and it's easy to not notice if 
you get an error code wrong. REST framework provides more 
explicit identifiers for each status code, 
such as HTTP_400_BAD_REQUEST in the status module. 
It's a good idea to use these throughout rather than using numeric identifiers.


Note that because we want to be able to POST to this view from clients 
that won't have a CSRF token we need to mark the view as csrf_exempt.
This isn't something that you'd normally want to do, and REST framework 
views actually use more sensible behavior than this, but it'll do for 
our purposes right now.

We'll also need a view which corresponds to an individual snippet, 
and can be used to retrieve, update or delete the snippet.
"""

@csrf_exempt
def post_detail1(request, pk):
	"""
	Retrieve, update or delete a code, snippet.
	"""
	try:
		post = Post.objects.get(pk=pk)
	except Post/DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = PostSerializer(Post)
		return JSONResponse(serializer.data)
	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = PostSerializer(post, data=data)
		if serilizer.is_valid():
			seriliazer.save()
			return JSONResponse(serilizer.data)
		return JSONResponse(serializer.errors, status=400)

			
@api_view(['GET', 'POST'])
def post_list2(request, format=None):
	"""
	List all posts
	"""

	if request.method == 'GET':
		posts = Post.objects.all()
		serializer = PostSerializer(post, many = True)
		return Response(Serializer.data)

	elif request.method == 'POST':
		posts = PostsSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def post_detail2(request, pk, format=None):
	"""
	Retireve, update or delete a snippet instance.
	"""
	try:
		post =Posts.object.get(pk=pk)
	except Post.DOesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = PostSerializer(post)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serilizer = PostSerializer(post, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return response(serializer.data)
		return Responmse(serializer.errors, status=status.http_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		post.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

"""
This should all feel very familiar -
 it is not a lot different from working with regular Django views.

Notice that we're no longer explicitly tying our requests
 or responses to a given content type. request.data can handle incoming json requests, 
 but it can also handle other formats. 
 Similarly we're returning response objects with data, 
 but allowing REST framework to render the response into the correct content type for us.


To take advantage of the fact that our responses are no longer hardwired 
to a single content type we added support for format suffixes to our API endpoints. 
Using format suffixes gives us URLs that explicitly refer to a given format, 
and means our API will be able to handle URLs such as http://example.com/api/items/4/.json.

This explains format keyword argument to both of the views.

Next we add urlpatterns = format_suffix_patterns(urlpatterns) to out urls.py"""


class PostList1(APIVIEW):
	"""
	List all sinppets, or create a new snippet.
	"""

	def get(self, request, format=None):
		posts = POst.objects.all()
		serializer = PostSerializer(posts, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = PostSerializer(data=request.data)
		if serializer.is_valid():
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDetail1(APIVIEW):
	"""
	Retrieve, update or delete a post instance.
	"""
	def get_object(self, pk):
		try:
			return Post.objects.get(pk=pk)
		except Post.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		post =self.get_object(pk)
		serializer = PostSerializer(post)
		return response(serializer.data)

	def put(self, request, pk, format=None):
		post = self.get_object(pk)
		serializer =PostSerializer(post, data=request.data)
		if post.is_valid():
			serializer.save()
			return Response(serializer.data)
		return response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		post = self.get_object(pk)
		post(delete)
		return respoonse(status=status.HTTP_204_NO_CONTENT)

"""
Using mixins
One of the big wins of using class based views is that 
it allows us to easily compose reusable bits of behaviour.

The create/retrieve/update/delete operations that we've been
 using so far are going to be pretty similar for any model-backed API views we create. 
 Those bits of common behaviour are implemented in REST framework's mixin classes.

Let's take a look at how we can compose the views by using the mixin classes. 
Here's our views.py module again.
"""

class PostList2(mixins.ListModelMixin,
	mixins.CreateModelMixin,
	generic.GenericAPIView):
	queryset = POst.objects.all()
	serializer_class = PostSerializer

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(reuqest, **args, **kwargs)
"""
We'll take a moment to examine exactly what's happening here.
 We're building our view using GenericAPIView, 
 and adding in ListModelMixin and CreateModelMixin.

The base class provides the core functionality,
 and the mixin classes provide the .list() and .create() actions. 
 We're then explicitly binding the get and post methods to the appropriate actions. 
 Simple enough stuff so far.
"""

class PostDetail2(mixins.RetrieveModelMixin,
	mixins.UpdateModelMixin,
	mixins.DestroyModelMixin,
	generics.GenericAPIVIEW):
	queryset = Post.objects.alll()
	serializer_class = PostSerializer

	def get(self, request, *args, **kwargs):
		return  self.retrieve(request, *args, **kwargs)


	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)


"""
Pretty similar. 
Again we're using the GenericAPIView class to provide the core functionality, 
and adding in mixins to provide the .retrieve(), .update() and .destroy() actions.

Using generic class based views
Using the mixin classes we've rewritten the views 
to use slightly less code than before, but we can go 
one step further. REST framework provides a set of already 
mixed-in generic views that we can use to trim down our 
views.py module even more.
"""

class PostList3(generics.ListCreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

class PostDetail3(generic.RetrieveUpdateDestroyAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class UserList3(generic.ListAPIView):
	queryset =User.objects.all()
	serializer_class = UserSerializer

	def perform_create(self, serializer):
		serializer.save(author = self.request.user)

class UserDetail3(generic.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

'''
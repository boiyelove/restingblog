from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
#from .views import PostViewSet, UserViewSet
from posts import views
from rest_framework.routers import DefaultRouter

"""
USING ROUTERS
Because we're using ViewSet classes rather than View classes,
we actually don't need to design the URL conf ourselves.
The conventions for wiring up resources into views and urls 
can be handled automatically, using a Router class. 
All we need to do is register the appropriate view sets
with a router, and let it do the rest.

Registering the viewsets with the router is similar to 
providing a urlpattern. We include two arguments - 
the URL prefix for the views, and the viewset itself.

The DefaultRouter class we're using also automatically 
creates the API root view for us, so we can now delete the 
api_root method from our views module.


TRADE-OFFS BETWEEN VIEWS VS VIEWSETS
Using viewsets can be a really useful abstraction.
It helps ensure that URL conventions will be consistent 
across your API, minimizes the amount of code you need to 
write, and allows you to concentrate on the interactions 
and representations your API provides rather than the 
specifics of the URL conf.

That doesn't mean it's always the right approach to take. 
There's a similar set of trade-offs to consider as when using
class-based views instead of function based views. 
Using viewsets is less explicit than building your views 
individually.

"""
#create a router and regiter por viewsets with it.
router = DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'users', views.UserViewSet)
urlpatterns = [
	url(r'^', include(router.urls)),
	]

"""
Complex Ways could include
Binding ViewSets to URLs explicitly
The handler methods only get bound to the 
actions when we define the URLConf. 
To see what's going on under the hood let's first 
explicitly create a set of views from our ViewSets.

In the urls.py file we bind our ViewSet classes 
into a set of concrete views.

Notice how we're creating multiple views from each
 ViewSet class, by binding the http methods to the 
 required action for each view.

Now that we've bound our resources into concrete views,
we can register the views with the URL conf as usual





post_list = PostViewSet.as_view({
	'get':'list',
	'post':'create'
	})
post_details = PostViewSet.as_view({
	'get':'retrieve',
	'put':'update',
	'patch':'partial_update',
	'delete':'destroy'
	})
user_list = UserViewSet.as_View({
	'get':'list'
	})
user_detail = UserViewSet.as_view({
	'get':'retrieve'
	})






urlpatters = format_suffix_patterns([
	url(r'^$', views.api_root),




USING VIEWSETS BOUND EXPLICITLY TO URLS
url(r'^posts/$', post_list, name='post-list'),
url(r'^posts/(?P<pk>[0-9]+)/$', post_detail, name='post-detail'),
url(r'^users/$', user_list, name ='user-list',
url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name = 'user-detail'),





FUNCTION BASED VIEWS
url(r'^post/$', views.post_list),
url(r'^posts/(?P<pk>[0-9]+)/$', views.post_detail),





USING CLASS BASED VIEWS
url(r'^posts/$', views.PostList.as_view(), name='post-list'),
url(r'^posts/(?P<pk>[0-9]+)/$', views.PostDetail.as_view(), name='post-detail'),
url(r'^users/$', views.UserList.as_view()), name ='user-list',
url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name = 'user-detail'),
])




The above is same as urlpatterns = format_suffix_patterns(urlpatterns)
We don't necessarily need to add these extra url patterns in, 
but it gives us a simple, clean way of referring to a specific format.
"""




from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.BlogIndexView.as_view(), name="blog_index"),
	url(r'^search/(?P<search>[\w]+)/$', views.SearchView.as_view(), name="blog_search"),
	url(r'^posts/$', views.PostListView.as_view(), name="blog_post_list"),
	url(r'^posts/create/$', views.PostCreateView.as_view(), name="blog_post_create"),
	url(r'^posts/(?P<pk>[\d]+)/$', views.PostDetailView.as_view()),
	url(r'^posts/(?P<slug>[\w]+)/$', views.PostDetailView.as_view(), name="blog_post_detail"),
	url(r'^posts/(?P<slug>[\w]+)/edit/$', views.PostUpdateView.as_view(), name="blog_post_edit"),
	url(r'^posts/(?P<slug>[\w]+)/delete/$', views.PostDeleteView.as_view(), name="blog_post_delete"),
	url(r'^category/$', views.CategoryListView.as_view(), name="blog_category_List"),
	url(r'^category/create/$', views.CategoryCreateView.as_view(), name="blog_category_create"),
	url(r'^category/(?P<pk>[\d]+)/$', views.CategoryDetailView.as_view()),
	url(r'^category/(?P<slug>[\w]+)/$', views.CategoryDetailView.as_view(), name="blog_category_detail"),
	url(r'^category/(?P<slug>[\w]+)/edit/$', views.CategoryUpdateView.as_view(), name="blog_category_edit"),
	url(r'^category/(?P<slug>[\w]+)/delete/$', views.CategoryDeleteView.as_view(), name="blog_category_delete"),	
	]
# urls.py in blog project for potato
# created by Puneet Chawla (pchawla@buffalo.edu)

from django.conf.urls.defaults import *

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
# blank url for home page
    url(r'^$', 'blog.views.home'),
    url(r'^home/$', 'blog.views.home'),
    url(r'^blog/newblog/goto_create/$', 'blog.views.create_page'),
    url(r'^blog/newblog/create/$', 'blog.views.create_blog'),
# to view blog page goto /blog/(blogname)/
# but can also visit directly by /(blogname)/
    url(r'^(?P<blog_name>[^/]+)/$', 'blog.views.view_blog'),
    url(r'^blog/(?P<blog_name>[^/]+)/$', 'blog.views.view_blog'),
    url(r'^blog/(?P<blog_name>[^/]+)/edit/$', 'blog.views.edit_blog'),
    url(r'^blog/(?P<blog_name>[^/]+)/save/$', 'blog.views.save_blog'),
    url(r'^blog/(?P<blog_name>[^/]+)/delete/$', 'blog.views.delete_blog'),
    url(r'^blog/(?P<blog_name>[^/]+)/deleteconfirm/$', 'blog.views.delete_confirm'),
)

# views.py in blog project for potato
# created by Puneet Chawla (pchawla@buffalo.edu)

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from blog.models import myblog

# creating method home and an instance 'b' of all the objects in db
# passing 'b' as parameter to view list of all the blogs in home page
def home(request):
    b=myblog.objects.all()
    return render_to_response('blog/home.html',{'blogslist':b})

# simply pointing it to "blog/create.html" with proper csrf token request
def create_page(request):
    return render_to_response('blog/create.html',context_instance=RequestContext(request))

# this method checks if title has been entered in the create form
# then it checks if blog (object) already exist in db
# if no then it creates the new blog (object) with title as primary keys
def create_blog(request):
    title=request.POST["title"]
    if title:
        content=request.POST["content"]
        try:
            blog=myblog.objects.get(pk=title)
            return HttpResponse ("This Blog Already Exist! Please select and edit it from the list")
        except myblog.DoesNotExist:
            newblog=myblog(title=title, content=content)
            newblog.save()
            return HttpResponseRedirect("/blog/"+title+"/")
    else:
        return HttpResponse ("Please enter a valid Title!")

# this method checks if requested blog existes or not
# if exists it point to the view.html with the asked blog (object) to show the details of it
def view_blog(request, blog_name):
    try:
        blog=myblog.objects.get(pk=blog_name)
        content=blog.content
        return render_to_response("blog/view.html", {"blog": blog})
    except myblog.DoesNotExist:
        return HttpResponse ("This Blog Does Not Exist! Please choose from the given list")
#        return render_to_response("blog/create.html",{"blogname":blog_name})

# this module checks if blog exists
# and pass the current content to edit page
def edit_blog(request, blog_name):
    try:
        blog = myblog.objects.get(pk=blog_name)
        content = blog.content
    except myblog.DoesNotExist:
        return HttpResponse ("This Blog Does Not Exist! Please choose from the given list")
    return render_to_response("blog/edit.html", {"blog_name":blog_name, "content":content}, context_instance=RequestContext(request))

# this module saves the updated content of the existing blog
def save_blog(request, blog_name):
    content=request.POST["content"]
    try:
        blog = myblog.objects.get(pk=blog_name)
        blog.content = content
    except myblog.DoesNotExist:
        return HttpResponse ("This Blog Does Not Exist! Please choose from the given list")
    blog.save()
    return HttpResponseRedirect("/blog/" + blog_name + "/") 

# this module checks if the blog exists and return to delete.html to get confirmation on deleteing the blog (object) from db
def delete_blog(request, blog_name):
    try:
        blog=myblog.objects.get(pk=blog_name)
        content=blog.content
        return render_to_response("blog/delete.html", {"blog": blog})
    except myblog.DoesNotExist:
        return HttpResponse ("This Blog Does Not Exist! Please choose from the given list")

# ones given the confirmation this module deletes the blog (object) from db
# and retuen to home page
def delete_confirm(request, blog_name):
    blog=myblog.objects.get(pk=blog_name)
    blog.delete()
    return HttpResponseRedirect("/home/")

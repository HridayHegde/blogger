from django.shortcuts import render
from django.shortcuts import redirect
from  blogging.models import *
from django.contrib.auth import authenticate, login
# Create your views here.
import sys
import logging

from django.conf import settings
from django.shortcuts import redirect

logger = logging.getLogger(__name__)


def HomePage(request):
    try:
        if not request.user.is_authenticated:
            return redirect(login_user)
        user = UserDetails.objects.get(user=request.user)
        blogs = BlogPost.objects.filter(user=user, is_deleted=False)
        return render(request,'blogging/index.html', {'blogs':blogs, 'userdetails':user})
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.error("HomePage %s at line %s",str(e),str(exc_tb.tb_lineno))


def SetBlogDetails(request):
    try:
        if not request.user.is_authenticated:
            return redirect(login_user)
        
        if request.method == 'POST':
            categories = request.POST.getlist('categories')
            title = request.POST.get('title')
            content = request.POST.get('content')
            blog_id = request.POST.get('blog_id')

            blog_object = BlogPost.objects.filter(id=blog_id)
            if len(blog_object) > 0:
                blog_object = blog_object[0]
                blog_object.title = title
                blog_object.content = content
                category_list =[]
                for id in categories:
                    category_list.append(Category.objects.get(id=id))
                blog_object.category.set(category_list) 
                blog_object.save()
                return  redirect(HomePage)
            else:
                return  redirect(HomePage)
        else:
            return redirect(HomePage)

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.error("HomePage %s at line %s",str(e),str(exc_tb.tb_lineno))


def EditBlog(request, id):
    try:
        if not request.user.is_authenticated:
            return redirect(login_user)
        blog_object = BlogPost.objects.filter(id=id)
        user = UserDetails.objects.get(user=request.user)
        categories = Category.objects.filter(user=request.user,  is_deleted=False)
       
        if len(blog_object) <= 0:
            return redirect(HomePage)     
        else:
            blog_object = blog_object[0]
            selected_categories = list(blog_object.category.all().values_list('id',flat=True))
            return render(request,'blogging/editblog.html', {'blog':blog_object, 'userdetails':user, 'categories':categories,'selected_categories':selected_categories})

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.error("HomePage %s at line %s",str(e),str(exc_tb.tb_lineno))


def DeleteBlog(request, id):
    try:
        if not request.user.is_authenticated:
            return redirect(login_user)
        blog_object = BlogPost.objects.filter(id=id)
        if len(blog_object) <0:
            return redirect(HomePage) 
        else:
            blog_object = blog_object[0]
            blog_object.is_deleted = True
            blog_object.save()
            return redirect(HomePage) 

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.error("HomePage %s at line %s",str(e),str(exc_tb.tb_lineno))

def login_user(request):
    try:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(HomePage)
            else:
                return render(request,'blogging/login.html', {'error':"Incorrect Username or password"})
        else:
            return render(request,'blogging/login.html')
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.error("Login User %s at line %s",str(e),str(exc_tb.tb_lineno))
        return render(request,'blogging/login.html')
    
def PostABlog(request):
    try:
        if not request.user.is_authenticated:
            return redirect(login_user)
        
        categories = Category.objects.filter(user=request.user,  is_deleted=False)
        return render(request, 'blogging/createblog.html', {'categories':categories})
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.error("HomePage %s at line %s",str(e),str(exc_tb.tb_lineno))

def CreateNewBlog(request):
    try:
        if not request.user.is_authenticated:
            return redirect(login_user)
        categories = request.POST.getlist('categories')
        title = request.POST.get('title')
        content = request.POST.get('content')
        publish = request.POST.get('publish')
        print(publish)
        category_list =[]
        for id in categories:
            category_list.append(Category.objects.get(id=id))
        if publish == 'on':
            publish = True
        else:
            publish = False
        blog_object = BlogPost.objects.create(title=title,content=content, user=UserDetails.objects.get(user=request.user),is_publised=publish)
        blog_object.category.set(category_list)
        blog_object.save()
        return redirect(HomePage)

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.error("CreateNewBlog %s at line %s",str(e),str(exc_tb.tb_lineno))

def EditCategories(request):
    try:
        if not request.user.is_authenticated:
            return redirect(login_user)
        
        user = UserDetails.objects.get(user=request.user)
        categories = Category.objects.filter(user=request.user, is_deleted=False)
        return render(request,'blogging/editcategories.html', {'categories':categories})

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.error("EditCategories %s at line %s",str(e),str(exc_tb.tb_lineno))


def DeleteCategory(request,id):
    try:
        if not request.user.is_authenticated:
            return redirect(login_user)
        
        user = UserDetails.objects.get(user=request.user)
        category = Category.objects.filter(id=id)
        if len(category) >0:
            category = category[0]
            category.is_deleted = True
            category.save()

        return redirect(EditCategories)

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.error("DeleteCategory %s at line %s",str(e),str(exc_tb.tb_lineno))

def SetCategory(request,id):
    try:
        if not request.user.is_authenticated:
            return redirect(login_user)
        
        if request.method == 'POST':
            category_name = request.POST.get('category_name')
            user = UserDetails.objects.get(user=request.user)
            category = Category.objects.filter(id=id)
            if len(category) >0:
                category = category[0]
                category.category_name = category_name
                category.save()

        return redirect(EditCategories)

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.error("SetCategory %s at line %s",str(e),str(exc_tb.tb_lineno))


def CreateCategory(request):
    try:
        if not request.user.is_authenticated:
            return redirect(login_user)
        
        if request.method == 'POST':
            category_name = request.POST.get('category_name')
            category = Category.objects.filter(category_name=category_name, is_deleted=False)
            if len(category) >0:
                return redirect(EditCategories)
            else:
                category_item = Category.objects.create(category_name=category_name,user=request.user)
                return redirect(EditCategories)


    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.error("SetCategory %s at line %s",str(e),str(exc_tb.tb_lineno))
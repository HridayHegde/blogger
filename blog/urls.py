"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include

from blogging import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.HomePage, name="HomePage"),
    re_path(r'^login/$', views.login_user, name='login_user'),
    path("__reload__/", include("django_browser_reload.urls")),
    re_path(r'^delete/(?P<id>\d+)/$',views.DeleteBlog, name="delete_blog"),
    re_path(r'^edit/(?P<id>\d+)/$',views.EditBlog, name="edit_blog"),
    path('setblogdetails/', views.SetBlogDetails, name="SetBlogDetails"),
    path('createblog/', views.CreateNewBlog, name="createnewblog"),
    path('postablog/', views.PostABlog, name="postablog"),
    path('editcategories/', views.EditCategories, name="editcategories"),
    re_path(r'^deletecategory/(?P<id>\d+)/$',views.DeleteCategory, name="deletecategory"),
    re_path(r'^setcategory/(?P<id>\d+)/$',views.SetCategory, name="setcategory"),
    path('addcategory/', views.CreateCategory, name="addcategory"),
]

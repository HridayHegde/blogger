from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, help_text="Name of the user")
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "UserDetail"
        verbose_name_plural = "UserDetails"

class Category(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    is_deleted = models.BooleanField(default=False)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    category_name = models.CharField(max_length=255, help_text='Category name')

    def __str__(self):
        return self.category_name
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    

class BlogPost(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    published_at = models.DateTimeField(default=timezone.now)
    is_publised = models.BooleanField(default=False)
    edited_at = models.DateTimeField(default=timezone.now)
    is_deleted = models.BooleanField(default=False)
    category = models.ManyToManyField(Category, blank=True, help_text="categories")
    user = models.ForeignKey(UserDetails,null=True,on_delete=models.SET_NULL)

    #Blog data
    title = models.TextField(help_text="Title of the blogpost")
    content = models.TextField(help_text="Content of the blogpost")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "BlogPost"
        verbose_name_plural = "BlogPosts"
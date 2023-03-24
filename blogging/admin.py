from django.contrib import admin
from blogging.models import *
# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('created_at','published_at', 'user','title','is_publised','is_deleted')
    search_fields =('title','category',)

admin.site.register(BlogPost, BlogPostAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('created_at','category_name','is_deleted')
    search_fields =('category_name',)

admin.site.register(Category, CategoryAdmin)

class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ('user','name')
    search_fields =('name',)

admin.site.register(UserDetails, UserDetailsAdmin)
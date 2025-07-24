from django.contrib import admin
from .models import Post
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_published', 'is_editorschoice', 'date_created')
    list_editable = ('is_published', 'is_editorschoice')
    
admin.site.register(Post, PostAdmin)

# Register your models here.

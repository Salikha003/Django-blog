from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author')
    # list_display_links = ('id', 'title', 'author')
    ordering = ['-title']
    list_editable = ( 'author',)
    # list_per_page = 2
    search_fields = ('title', )




# admin.site.register(Post, PostAdmin)


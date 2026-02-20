from django.contrib import admin
from .models import Posts

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'author')

admin.site.register(Posts, PostAdmin)
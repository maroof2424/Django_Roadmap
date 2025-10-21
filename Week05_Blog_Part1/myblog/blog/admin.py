from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ("user","title","content","created_at","updated_at")
    search_fields = ("user","title","content")
    list_filter = ('created_at','updated_at')
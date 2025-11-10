from django.contrib import admin
from .models import Todo
# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = ("title","descrption","complete","created_at")
    list_filter = ("complete","created_at")
    search_fields = ("title","description")

    
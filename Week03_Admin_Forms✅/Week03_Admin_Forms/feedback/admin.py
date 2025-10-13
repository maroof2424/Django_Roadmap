from django.contrib import admin
from .models import Feedback

# Register your models here.

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name','email','rating','created_at')
    search_fields = ('name','email')
    list_filter = ('rating','created_at')
from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Category, Tutorial

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'icon')
    prepopulated_fields = {'slug': ('name',)} # Remplissage auto du slug

@admin.register(Tutorial)
class TutorialAdmin(MarkdownxModelAdmin): # Active la preview Markdown
    list_display = ('title', 'category', 'created_at', 'is_published')
    list_filter = ('is_published', 'category')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
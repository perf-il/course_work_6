from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_name', 'slug', 'content', 'data_creating', 'is_published',)
    prepopulated_fields = {'slug': ('title_name',)}
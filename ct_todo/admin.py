from django.contrib import admin
from . models import Task, Category

# Register your models here.
admin.site.register(Task)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass